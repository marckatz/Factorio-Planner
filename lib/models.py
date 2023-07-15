#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, Float, Boolean, Table, ForeignKey, MetaData, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
engine = create_engine('sqlite:///factorio.db')
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

# recipe_ingredient = Table(
#     'recipe_ingredients',
#     Base.metadata,
#     Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
#     Column('ingredient_id', ForeignKey('ingredients.id'), primary_key=True),
#     extent_existing=True,
# )

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    machine_type_id = Column(Integer())
    tier_min = Column(Integer())
    time = Column(Float())
    
    ingredients = relationship('RecipeIngredient', back_populates='recipe')

    def __repr__(self):
        return f'<Recipe id={self.id} name=\'{self.name}\'>'

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    recipes = relationship('RecipeIngredient', back_populates='ingredient')

    def __repr__(self):
        return f'<Ingredient id={self.id} name=\'{self.name}\'>'

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(Integer(), primary_key=True)
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))
    amount = Column(Integer())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))
    is_input = Column(Boolean())

    ingredient = relationship('Ingredient', back_populates='recipes')
    recipe = relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return '<RecipeIngredient id={} ingredient=\'{}\' amount={} recipe=\'{}\' {}put>'.format(
            self.id,
            self.ingredient.name,
            self.amount,
            self.recipe.name,
            'in' if self.is_input else 'out'
        )