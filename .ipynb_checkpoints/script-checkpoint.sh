#!/bin/bash

for dir in Raw_Songs_DataBase/*; do 
    # Check if "Songs" subdirectory exists
    if [ -d "$dir/Songs" ]; then
        echo "$dir"
        # Store the current working directory
        current_directory=$(pwd)
        # Move to the "Songs" subdirectory
        cd "$dir/Songs"
        
        # Iterate through songs in the "Songs" subdirectory
        for song in *; do
            # Process each song using rid and redirect output to RID file
            cat "$song" | rid > "${song}_RID"
        done
        
        # Move back to the parent directory
        cd "$current_directory"
    fi
done