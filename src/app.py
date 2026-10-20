from decimal import Decimal

import streamlit as st

from src.repositories.material_repository import (
    criar_material,
    listar_materiais,
)
from src.repositories.variacao_material_repository import (
    criar_variacao,
    listar_variacoes,
)
st.set_page_config(
    page_title="EntreTrama",
    page_icon="🧶",
    layout="wide",
)

st.title("EntreTrama")
st.caption("Gestão integrada para negócios artesanais")

st.divider()

st.header("Cadastro de materiais")

with st.form("formulario_material", clear_on_submit=True, enter_to_submit=False,):
    nome = st.text_input("Nome do material")
    marca = st.text_input("Marca (opcional)")

    categoria = st.selectbox(
        "Categoria",
        [
            "Fios",
            "Ferragens",
            "Tecidos",
            "Enchimentos",
            "Embalagens",
            "Outros",
        ],
    )

    unidade_controle = st.selectbox(
        "Unidade de controle",
        ["g", "un"],
        format_func=lambda unidade: {
            "g": "Gramas (g)",
            "un": "Unidades (un)",
        }[unidade],
    )

    salvar = st.form_submit_button("Cadastrar material")

if salvar:
    if not nome.strip():
        st.error("Informe o nome do material.")
    else:
        try:
            criar_material(
                nome=nome.strip(),
                categoria=categoria,
                unidade_controle=unidade_controle,
                marca=marca.strip() or None,

            )
            st.success("Material cadastrado com sucesso!")
        except Exception as erro:
            st.error("Não foi possível cadastrar o material.")
            st.exception(erro)

st.divider()

st.subheader("Materiais cadastrados")

try:
    materiais = listar_materiais()

    if materiais:
        dados = [
            {
                "ID": material.id,
                "Material": material.nome,
                "Marca": material.marca or "Não informada",
                "Categoria": material.categoria,
                "Unidade": material.unidade_controle,
                "Ativo": "Sim" if material.ativo else "Não",
            }
            for material in materiais
        ]

        st.dataframe(
            dados,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Nenhum material cadastrado ainda.")

except Exception as erro:
    st.error("Não foi possível consultar os materiais.")
    st.exception(erro)

st.divider()

st.header("Cadastro de variações")

materiais_disponiveis = listar_materiais()

if not materiais_disponiveis:
    st.info("Cadastre um material antes de adicionar variações.")

else:
    materiais_por_id = {
        material.id: material
        for material in materiais_disponiveis
    }

    with st.form(
        "formulario_variacao",
        clear_on_submit=True,
        enter_to_submit=False,
    ):
        material_id = st.selectbox(
            "Material",
            options=list(materiais_por_id.keys()),
            format_func=lambda id: (
                f"{materiais_por_id[id].nome} — "
                f"{materiais_por_id[id].marca or 'Sem marca'}"
            ),
        )

        descricao = st.text_input(
            "Variação (cor, tamanho ou modelo)"
        )

        codigo_referencia = st.text_input(
            "Código de referência (opcional)"
        )

        estoque_minimo = st.number_input(
            "Estoque mínimo",
            min_value=0.0,
            value=0.0,
            step=1.0,
        )

        st.caption(
            "O estoque mínimo usa a unidade de controle "
            "do material selecionado."
        )

        salvar_variacao = st.form_submit_button(
            "Cadastrar variação"
        )

    if salvar_variacao:
        if not descricao.strip():
            st.error("Informe a descrição da variação.")
        else:
            try:
                criar_variacao(
                    material_id=material_id,
                    descricao=descricao.strip(),
                    codigo_referencia=(
                        codigo_referencia.strip() or None
                    ),
                    estoque_minimo=Decimal(
                        str(estoque_minimo)
                    ),
                )

                st.success("Variação cadastrada com sucesso!")

            except Exception as erro:
                st.error("Não foi possível cadastrar a variação.")
                st.exception(erro)

st.subheader("Variações cadastradas")

try:
    variacoes = listar_variacoes()

    if variacoes:
        materiais_por_id = {
            material.id: material
            for material in listar_materiais()
        }

        dados_variacoes = []

        for variacao in variacoes:
            material = materiais_por_id.get(
                variacao.material_id
            )

            if material is None:
                continue

            dados_variacoes.append({
                "Material": material.nome,
                "Marca": material.marca or "Não informada",
                "Variação": variacao.descricao,
                "Código": variacao.codigo_referencia or "—",
                "Estoque mínimo": float(variacao.estoque_minimo),
                "Unidade": material.unidade_controle,
            })

        st.dataframe(
            dados_variacoes,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.info("Nenhuma variação cadastrada ainda.")

except Exception as erro:
    st.error("Não foi possível consultar as variações.")
    st.exception(erro)
