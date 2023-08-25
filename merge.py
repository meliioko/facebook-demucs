from pydub import AudioSegment


def merge(dir, name, offset):
    # Load the individual tracks
    vocals = AudioSegment.from_file(dir + "vocals.mp3")
    other = AudioSegment.from_file(dir + "other.mp3")
    bass = AudioSegment.from_file(dir + "bass.mp3")
    drums = AudioSegment.from_file(dir + "drums.mp3")

    # Ensure all audio segments are of the same length (optional, but might be necessary in some cases)
    min_length = min(len(vocals), len(drums), len(bass), len(other))
    vocals = vocals[:min_length]
    drums = drums[:min_length]
    bass = bass[:min_length]
    other = other[:min_length]

    vocals = vocals + int(offset)
    # Combine the tracks
    combined = vocals.overlay(drums).overlay(bass).overlay(other)

    # Export the combined track
    combined.export(name, format="mp3")


if __name__ == '__main__':
    import sys
    merge(sys.argv[1], sys.argv[2], sys.argv[3])
