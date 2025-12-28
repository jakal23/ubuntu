import os
import json
import subprocess
from datetime import datetime, timezone

# Supported media extensions
IMAGE_EXTS = [".jpg", ".jpeg", ".png", ".heic"]
VIDEO_EXTS = [".mp4", ".mov", ".mkv", ".avi"]

def find_metadata_file(media_file):
    """
    Try to find the matching metadata JSON file for the given image/video.
    Supports both '.supplemental-metadata.json' and '.supplemental-met.json' suffixes.
    """
    candidates = [
        f"{media_file}.supplemental-metadata.json",
        f"{media_file}.supplemental-met.json"
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate
    return None


def apply_metadata(media_file):
    meta_file = find_metadata_file(media_file)
    if not meta_file:
        print(f"⚠️ No metadata found for {media_file}")
        return

    with open(meta_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    # Prefer photoTakenTime if available, else fallback to creationTime
    ts = None
    if "photoTakenTime" in metadata and "timestamp" in metadata["photoTakenTime"]:
        ts = metadata["photoTakenTime"]["timestamp"]
    elif "creationTime" in metadata and "timestamp" in metadata["creationTime"]:
        ts = metadata["creationTime"]["timestamp"]

    if not ts:
        print(f"⚠️ No timestamp found in {meta_file}")
        return

    # Convert timestamp to UTC formatted date string
    taken_time = datetime.fromtimestamp(int(ts), tz=timezone.utc)
    formatted_time = taken_time.strftime("%Y:%m:%d %H:%M:%S")

    # Prepare exiftool command depending on type
    ext = os.path.splitext(media_file)[1].lower()

    cmd = ["exiftool"]
    if ext in IMAGE_EXTS:
        cmd += [
            f"-DateTimeOriginal={formatted_time}",
            f"-CreateDate={formatted_time}",
            f"-ModifyDate={formatted_time}"
        ]
    elif ext in VIDEO_EXTS:
        cmd += [
            f"-CreationDate={formatted_time}",
            f"-MediaCreateDate={formatted_time}",
            f"-TrackCreateDate={formatted_time}",
            f"-ModifyDate={formatted_time}"
        ]
    else:
        print(f"⚠️ Skipping unsupported file type: {media_file}")
        return

    # Add geo location if present and valid
    geo = metadata.get("geoData", {})
    lat, lon = geo.get("latitude"), geo.get("longitude")
    if lat and lon and (lat != 0 or lon != 0):
        cmd += [f"-GPSLatitude={lat}", f"-GPSLongitude={lon}"]

    # Output file overwrite in place
    cmd += ["-overwrite_original", media_file]

    # Run exiftool command
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Applied metadata to {media_file}")
    else:
        print(f"❌ Failed for {media_file}: {result.stderr}")


if __name__ == "__main__":
    for filename in os.listdir("."):
        ext = os.path.splitext(filename)[1].lower()
        if ext in IMAGE_EXTS + VIDEO_EXTS:
            apply_metadata(filename)
import os
import json
import subprocess
from datetime import datetime, timezone

# Supported media extensions
IMAGE_EXTS = [".jpg", ".jpeg", ".png", ".heic"]
VIDEO_EXTS = [".mp4", ".mov", ".mkv", ".avi"]

def find_metadata_file(media_file):
    """
    Try to find the matching metadata JSON file for the given image/video.
    Supports both '.supplemental-metadata.json' and '.supplemental-met.json' suffixes.
    """
    candidates = [
        f"{media_file}.supplemental-metadata.json",
        f"{media_file}.supplemental-met.json"
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate
    return None


def apply_metadata(media_file):
    meta_file = find_metadata_file(media_file)
    if not meta_file:
        print(f"⚠️ No metadata found for {media_file}")
        return

    with open(meta_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    # Prefer photoTakenTime if available, else fallback to creationTime
    ts = None
    if "photoTakenTime" in metadata and "timestamp" in metadata["photoTakenTime"]:
        ts = metadata["photoTakenTime"]["timestamp"]
    elif "creationTime" in metadata and "timestamp" in metadata["creationTime"]:
        ts = metadata["creationTime"]["timestamp"]

    if not ts:
        print(f"⚠️ No timestamp found in {meta_file}")
        return

    # Convert timestamp to UTC formatted date string
    taken_time = datetime.fromtimestamp(int(ts), tz=timezone.utc)
    formatted_time = taken_time.strftime("%Y:%m:%d %H:%M:%S")

    # Prepare exiftool command depending on type
    ext = os.path.splitext(media_file)[1].lower()

    cmd = ["exiftool"]
    if ext in IMAGE_EXTS:
        cmd += [
            f"-DateTimeOriginal={formatted_time}",
            f"-CreateDate={formatted_time}",
            f"-ModifyDate={formatted_time}"
        ]
    elif ext in VIDEO_EXTS:
        cmd += [
            f"-Keys:CreationDate={formatted_time}",
            f"-QuickTime:CreateDate={formatted_time}",
            f"-QuickTime:ModifyDate={formatted_time}",
            f"-TrackCreateDate={formatted_time}",
            f"-MediaCreateDate={formatted_time}",
            f"-TrackModifyDate={formatted_time}",
            f"-MediaModifyDate={formatted_time}"
    ]
    else:
        print(f"⚠️ Skipping unsupported file type: {media_file}")
        return

    # Add geo location if present and valid
    geo = metadata.get("geoData", {})
    lat, lon = geo.get("latitude"), geo.get("longitude")
    if lat and lon and (lat != 0 or lon != 0):
        cmd += [f"-GPSLatitude={lat}", f"-GPSLongitude={lon}"]

    # Output file overwrite in place
    cmd += ["-overwrite_original", media_file]

    # Run exiftool command
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Applied metadata to {media_file}")
    else:
        print(f"❌ Failed for {media_file}: {result.stderr}")


if __name__ == "__main__":
    for filename in os.listdir("."):
        ext = os.path.splitext(filename)[1].lower()
        if ext in IMAGE_EXTS + VIDEO_EXTS:
            apply_metadata(filename)
