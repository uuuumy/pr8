def justify_text(text, width):
    words = text.split()
    if not words:
        return []

    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if (current_length + len(word) + len(current_line) <= width):
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                lines.append(format_line(current_line, width, current_length))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def format_line(words, width, total_chars):
    if len(words) == 1:
        return words[0]

    spaces_needed = width - total_chars
    gaps = len(words) - 1
    base_spaces = spaces_needed // gaps
    extra_spaces = spaces_needed % gaps

    result = words[0]
    for i in range(1, len(words)):
        spaces = base_spaces + (1 if i <= extra_spaces else 0)
        result += ' ' * spaces + words[i]

    return result

text = input("")
width = int(input("Введите ширину строки: "))
lines = justify_text(text, width)
for line in lines:
    print(f"{line}")