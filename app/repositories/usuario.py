"""Acesso aos dados de usuário."""

from __future__  import annotations

from app.models import Usuario
from app.repositories import RepositorioBase


class UsuarioRepositorio(RepositorioBase[Usuario]):
    """Acesso aos dados de usúario."""

    @property
    def modelo(self) -> type[Usuario]:
        return Usuario

    def buscar_por_email(self,email:str) -> Usuario| None:
        """Busca pelo e-mail, normalizado como o modelo normaliza ao gravar.
        
        Sem a normalização, um cadastro feito com `"Ana@exemplo.com"` não seria
        encontrado por uma busca com `"ana@exemplo.com"`.
        """

        return (
            self._sessao.query(Usuario)
            .filter(Usuario.email == Usuario.normalizar_email(email))
            .first()
        )