from pydantic import BaseModel

class MoleculeBase(BaseModel):
    molecule_name: str

class MoleculeCreate(MoleculeBase):
    pass

class MoleculeUpdate(MoleculeBase):
    pass

class Molecule(MoleculeBase):
    id: int

    class Config:
        orm_mode = True