from sqlalchemy.orm import Session
from backend.models.common.molecule import Molecule as MoleculeModel
from backend.schemas.common.molecule import MoleculeCreate, MoleculeUpdate

def get_molecule(db: Session, molecule_id: int):
    return db.query(MoleculeModel).filter(MoleculeModel.id == molecule_id).first()

def get_molecules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MoleculeModel).offset(skip).limit(limit).all()

def create_molecule(db: Session, molecule: MoleculeCreate):
    db_molecule = MoleculeModel(molecule_name=molecule.molecule_name)
    db.add(db_molecule)
    db.commit()
    db.refresh(db_molecule)
    return db_molecule

def update_molecule(db: Session, molecule_id: int, molecule: MoleculeUpdate):
    db_molecule = get_molecule(db, molecule_id)
    if db_molecule:
        db_molecule.molecule_name = molecule.molecule_name
        db.commit()
        db.refresh(db_molecule)
    return db_molecule

def delete_molecule(db: Session, molecule_id: int):
    db_molecule = get_molecule(db, molecule_id)
    if db_molecule:
        db.delete(db_molecule)
        db.commit()
    return db_molecule