def fix_commas_in_place(filename="new.csv"):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fixed_lines = []
    for line in lines:
        parts = line.strip().split(',')

        if len(parts) == 3:
            # Merge first two fields
            merged = f'"{parts[0].strip()} {parts[1].strip()}",{parts[2].strip()}'
            fixed_lines.append(merged + '\n')

        elif len(parts) == 4:
            # Merge first three fields
            merged = f'"{parts[0].strip()} {parts[1].strip()} {parts[2].strip()}",{parts[3].strip()}'
            fixed_lines.append(merged + '\n')

        else:
            # Leave all other lines unchanged
            fixed_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(fixed_lines)

    print(f"✅ Fixed lines with 3 or 4 comma-separated values. Updated '{filename}' in place.")

if __name__ == "__main__":
    fix_commas_in_place()
