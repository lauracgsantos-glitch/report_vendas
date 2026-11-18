"""Verificação inicial do ambiente; sem acesso a serviços externos."""

import sys


def main() -> int:
    if sys.version_info < (3, 12):
        print("Este projeto requer Python 3.12 ou superior.", file=sys.stderr)
        return 1

    print("Ambiente report_vendas pronto para desenvolvimento.")
    print("Próxima etapa: definir a fonte de vendas, os indicadores e o canal do Slack.")
    print("As integrações e o agendamento ainda não estão implementados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
