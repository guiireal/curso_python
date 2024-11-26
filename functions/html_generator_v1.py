def block_tag(text, class_name="success"):
    return f'<div class="{class_name}">{text}</div>'


if __name__ == "__main__":
    assert (
        block_tag("Incluído com sucesso")
        == '<div class="success">Incluído com sucesso</div>'
    )

    assert (
        block_tag("Impossível excluir!", "error")
        == '<div class="error">Impossível excluir!</div>'
    )
