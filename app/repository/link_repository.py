from app.db.models import LinkShortModel
from sqlalchemy.orm  import Session
from app.db.depends import  get_db_session
from app.schemas.schemas import Auth, LinkShortIn,  UserIn
from sqlalchemy.sql.expression import select
import random
import string

class RepositoryLink:
    def __init__(self,db_session:Session) :
        self.db_session = db_session
    
    def salve_link(self,link: LinkShortIn,user_id:int ):
        link_model = LinkShortModel(
            user_id = user_id,
            link_long = link.link_long,
            short_link = link.short_link
        )
        self.db_session.add(link_model)    
        self.db_session.commit()
        self.db_session.refresh(link_model)

        return link_model
    

    def generate_link_short(self):
        self.caracteres = string.ascii_letters + string.digits
        self.links_gerados = set()

        while True:
            novo_link = ''.join(random.sample(self.caracteres, 5))
            novo_link_completo = f'https://cap-zip.com/{novo_link}'

            if novo_link_completo not in self.links_gerados and not self.obter_short_link_generate(novo_link_completo):
                self.links_gerados.add(novo_link_completo)
                return novo_link_completo
    
    def list_all_short_link(self, user_id: int):
        query = select(LinkShortModel).where(LinkShortModel.user_id == user_id)
        resultado = self.db_session.execute(query).scalars().all()
        return resultado
    
    def obter_short_link_generate(self, link_long):
        query = select(LinkShortModel.short_link).where(
        LinkShortModel.link_long == link_long
    )
        short_link_result = self.db_session.execute(query).scalar()
    
        short_link = short_link_result if short_link_result else None
    
        return short_link
