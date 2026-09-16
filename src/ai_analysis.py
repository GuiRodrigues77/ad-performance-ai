def analisar_campanha(campanha):

    analises = []

    # Análise do ROAS
    if campanha["ROAS"] >= 3:
        analises.append(
            "O ROAS está muito bom, indicando um bom retorno sobre o investimento."
        )
    elif campanha["ROAS"] >= 2:
        analises.append(
            "O ROAS apresenta um resultado positivo, mas ainda existe espaço para otimização."
        )
    elif campanha["ROAS"] >= 1:
        analises.append(
            "O ROAS está baixo e a campanha precisa ser acompanhada com atenção."
        )
    else:
        analises.append(
            "A campanha está gerando retorno abaixo do investimento."
        )

    # Análise do CTR
    if campanha["CTR"] >= 3:
        analises.append(
            "O CTR indica um bom nível de interação com o anúncio."
        )
    else:
        analises.append(
            "O CTR pode ser melhorado testando novos criativos ou públicos."
        )

    # Análise do CPA
    if campanha["CPA"] <= 20:
        analises.append(
            "O custo por conversão está controlado."
        )
    else:
        analises.append(
            "O custo por conversão está elevado e pode exigir otimização."
        )

    # Recomendação
    if campanha["ROAS"] >= 3 and campanha["CPA"] <= 20:
        recomendacao = (
            "Manter a campanha e considerar um aumento gradual do investimento."
        )
    elif campanha["ROAS"] >= 2:
        recomendacao = (
            "Manter a campanha e testar pequenas otimizações."
        )
    else:
        recomendacao = (
            "Revisar público, criativo, orçamento e estratégia da campanha."
        )

    resultado = "\n".join(analises)

    return f"""
ANÁLISE DA CAMPANHA

{resultado}

RECOMENDAÇÃO:
{recomendacao}
"""