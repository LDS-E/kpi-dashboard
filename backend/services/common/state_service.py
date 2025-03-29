from sqlalchemy.orm import Session
from backend.models.common.state import State
from backend.schemas.common.state import StateCreate

def create_state(db: Session, state: StateCreate):
    db_state = State(name=state.name, country_id=state.country_id)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def get_state_by_id(db: Session, state_id: int):
    return db.query(State).filter(State.id == state_id).first()

def get_states_by_country(db: Session, country_id: int):
    return db.query(State).filter(State.country_id == country_id).all()
