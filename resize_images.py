from PIL import Image
import os

def main():
    source_dir = "/Users/admin/Its_not_a_book/master_csv/photos/"
    target_dir = "./assets/small_imgs/"

    for sub_folder in ("image_front", "image_back", "image_left", "image_right"):
        for i, picture in enumerate(os.listdir(os.path.join(source_dir, sub_folder))):
            if "jpg" not in picture:
                    continue
            with Image.open(os.path.join(source_dir, sub_folder, picture)) as img:
                resized = img.resize((818, 1000), Image.Resampling.LANCZOS)

                resized.save(f"{os.path.join(target_dir, sub_folder, picture)}")

if __name__ == "__main__":
    main()