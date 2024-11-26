def block_tag(text, class_name="success", inline=False):
    tag = "span" if inline else "div"

    return f'<{tag} class="{class_name}">{text}</{tag}>'


if __name__ == "__main__":
    print(block_tag("Incluído com sucesso"))
    print(block_tag("Impossível excluir!", "error", True))
    print(block_tag("Incluído com sucesso", inline=True))
    print(block_tag(text="Impossível excluir!", class_name="error", inline=True))
