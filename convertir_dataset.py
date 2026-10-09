
from pathlib import Path
import shutil

import cv2
import numpy as np
from PIL import Image


# À MODIFIER selon l'emplacement de ton dataset
SOURCE = Path("/dataset_eau")  # Dossier contenant train, valid, test
DEST = Path("dataset_eau_yolo")

SPLITS = ["train", "valid", "test"]


def trouver_masque(image_path):
    """Cherche un masque ayant le même nom que l'image."""
    candidats = [
        image_path.with_suffix(".png"),
        image_path.with_name(image_path.stem + "_mask.png"),
        image_path.with_name(image_path.stem + "_mask.PNG"),
    ]

    for candidat in candidats:
        if candidat.exists():
            return candidat

    return None


def convertir_masque(mask_path, label_path):
    """Convertit un masque binaire en polygones YOLO."""
    mask = np.array(Image.open(mask_path))

    # Les masques attendus sont en niveaux de gris.
    # Si le masque est RGB, on prend le premier canal.
    if mask.ndim == 3:
        mask = mask[:, :, 0]

    hauteur, largeur = mask.shape

    # Valeur 0 = fond ; toute valeur non nulle = eau.
    binaire = np.where(mask > 0, 255, 0).astype(np.uint8)

    contours, _ = cv2.findContours(
        binaire,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    annotations = []

    for contour in contours:
        # Ignore les petites régions de moins de 3 pixels².
        if cv2.contourArea(contour) < 3:
            continue

        # Réduit le nombre de points du contour.
        epsilon = 0.002 * cv2.arcLength(contour, True)
        polygone = cv2.approxPolyDP(
            contour, epsilon, True
        ).reshape(-1, 2)

        if len(polygone) < 3:
            continue

        # YOLO attend des coordonnées normalisées entre 0 et 1.
        coordonnees = []

        for x, y in polygone:
            xn = x / max(largeur - 1, 1)
            yn = y / max(hauteur - 1, 1)
            coordonnees.extend([xn, yn])

        # 0 = classe "water" dans YOLO.
        ligne = "0 " + " ".join(
            f"{v:.6f}" for v in coordonnees
        )
        annotations.append(ligne)

    # Un fichier vide est valide si le masque ne contient
    # aucune région d'eau exploitable.
    label_path.write_text(
        "\n".join(annotations),
        encoding="utf-8"
    )


def main():
    if not SOURCE.is_dir():
        raise FileNotFoundError(
            f"Dataset introuvable : {SOURCE.resolve()}"
        )

    total = 0
    sans_masque = []

    for split in SPLITS:
        dossier_source = SOURCE / split

        if not dossier_source.is_dir():
            print(f"Dossier absent, ignoré : {dossier_source}")
            continue

        dossier_images = DEST / "images" / split
        dossier_labels = DEST / "labels" / split

        dossier_images.mkdir(parents=True, exist_ok=True)
        dossier_labels.mkdir(parents=True, exist_ok=True)

        images = sorted([
            *dossier_source.glob("*.jpg"),
            *dossier_source.glob("*.jpeg"),
            *dossier_source.glob("*.JPG"),
            *dossier_source.glob("*.JPEG"),
        ])

        for image_path in images:
            mask_path = trouver_masque(image_path)

            if mask_path is None:
                sans_masque.append(str(image_path))
                continue

            with Image.open(image_path) as image:
                largeur_image, hauteur_image = image.size

            with Image.open(mask_path) as mask:
                largeur_mask, hauteur_mask = mask.size

            if (largeur_image, hauteur_image) != (
                largeur_mask, hauteur_mask
            ):
                print(f"Dimensions incompatibles : {image_path}")
                continue

            # Copie la photo, mais pas le masque PNG.
            shutil.copy2(
                image_path,
                dossier_images / image_path.name
            )

            label_path = dossier_labels / (
                image_path.stem + ".txt"
            )

            convertir_masque(mask_path, label_path)
            total += 1

        print(f"{split} : conversion terminée")

    # Crée la configuration YOLO.
    yaml_path = DEST / "data.yaml"
    yaml_path.write_text(
        "path: .\n"
        "train: images/train\n"
        "val: images/valid\n"
        "test: images/test\n\n"
        "names:\n"
        "  0: water\n",
        encoding="utf-8"
    )

    print(f"\nImages converties : {total}")
    print(f"Configuration créée : {yaml_path.resolve()}")

    if sans_masque:
        print(f"\nImages sans masque correspondant : {len(sans_masque)}")
        for nom in sans_masque[:10]:
            print(" -", nom)


if __name__ == "__main__":
    main()