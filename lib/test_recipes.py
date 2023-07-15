from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Recipe, RecipeIngredient, Ingredient

import ipdb

if __name__=='__main__':
    engine = create_engine('sqlite:///factorio.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()
    session.query(Ingredient).delete()

    ingredient_names = ['electronic circuit', 'iron plate', 'iron ore', 'copper wire',
                        'copper plate', 'copper ore']
    ingredients = {}
    for name in ingredient_names:
        ingredient = Ingredient(name=name)
        
        session.add(ingredient)
        session.commit()

        ingredients[name] = ingredient


    recipes = [
        Recipe(
            name='make electronic circuits',
            machine_type_id=1,#placeholder for assembling machine
            tier_min=1,
            time=0.5
        ),
        Recipe(
            name='make copper wire',
            machine_type_id=1,
            tier_min=1,
            time=0.5
        ),
        Recipe(
            name='smelt iron ore into plates',
            machine_type_id=2,
            tier_min=1,
            time=3.2
        ),
        Recipe(
            name='smelt copper ore into plates',
            machine_type_id=2,
            tier_min=1,
            time=3.2
        )
    ]
    for recipe in recipes:
        session.add(recipe)
        session.commit()


    #RecipeIngredients for electrionic circuits
    ec_recipe_ingredients=[
        RecipeIngredient(
            ingredient_id=ingredients['electronic circuit'].id,
            amount=1,
            recipe_id=recipes[0].id,
            is_input=False
        ),
        RecipeIngredient(
            ingredient_id=ingredients['iron plate'].id,
            amount=1,
            recipe_id=recipes[0].id,
            is_input=True
        ),
        RecipeIngredient(
            ingredient_id=ingredients['copper wire'].id,
            amount=3,
            recipe_id=recipes[0].id,
            is_input=True
        ),
    ]
    for ri in ec_recipe_ingredients:
        session.add(ri)
        session.commit()

    #RecipeIngredients for copper wire
    cw_recipe_ingredients = [
        RecipeIngredient(
            ingredient_id=ingredients['copper wire'].id,
            amount=2,
            recipe_id=recipes[1].id,
            is_input=False
        ),
        RecipeIngredient(
            ingredient_id=ingredients['copper plate'].id,
            amount=1,
            recipe_id=recipes[1].id,
            is_input=True
        )
    ]
    for ri in cw_recipe_ingredients:
        session.add(ri)
        session.commit()

    #RecipeIngredients for smelting
    smelting_recipe_ingredients = [
        RecipeIngredient(
            ingredient_id=ingredients['copper plate'].id,
            amount=1,
            recipe_id=recipes[2].id,
            is_input=False
        ),
        RecipeIngredient(
            ingredient_id=ingredients['copper ore'].id,
            amount=1,
            recipe_id=recipes[2].id,
            is_input=True
        ),
        RecipeIngredient(
            ingredient_id=ingredients['iron plate'].id,
            amount=1,
            recipe_id=recipes[3].id,
            is_input=False
        ),
        RecipeIngredient(
            ingredient_id=ingredients['iron ore'].id,
            amount=1,
            recipe_id=recipes[2].id,
            is_input=True
        ),
    ]
    for ri in smelting_recipe_ingredients:
        session.add(ri)
        session.commit()

    # ipdb.set_trace()

    session.close()