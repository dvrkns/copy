# Проверяем, есть ли хотя бы одна пара
        has_pairs = any(pair is not None for pair in pairs_raw)

        if not has_pairs:
            # Если пар нет, выводим сообщение о выходных
            lines.append("")
            lines.append("<b>Удачных выходных!</b>")
            return "\n".join(lines)

        lines.append("")
