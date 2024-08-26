zip_dir="benchmarks/zip_files"
dest_dir="benchmarks"

for zip_file in "$zip_dir"/*.zip; do
  # Unzip each file into the destination directory
  unzip -o "$zip_file" -d "$dest_dir"
done


