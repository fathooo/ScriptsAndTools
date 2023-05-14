import subprocess

INPUTFILE = "video.mkv"
OUTPUTFILE = "compressed_video.mkv"
FORMAT_OUTPUT = "mp4"

def compress_video(input_file, output_file):
    process = subprocess.Popen(["ffmpeg", "-y", "-i", input_file, "-c:v", "libx264", "-crf", "30", "-s", "1920x1080", "-c:a", "aac", "-q:a", "4", "-t", "45", "-f", "mp4", output_file])
    process.wait()
    print("Video comprimido exitosamente!")


if __name__ == "__main__":
    input_file = "video.mkv"
    output_file = "compressed_video." + FORMAT_OUTPUT
    compress_video(input_file, output_file)
