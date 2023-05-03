read -p "Enter directory path: " dir_path
if [ -d "$dir_path" ]; then
  tar -czvf archive.tar.gz "$dir_path"
else
  echo "Directory does not exist"
fi