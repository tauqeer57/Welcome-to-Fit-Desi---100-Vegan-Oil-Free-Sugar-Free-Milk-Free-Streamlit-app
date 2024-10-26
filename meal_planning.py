# meal_planning.py

import pandas as pd

def get_meal_options(meal_type: str):
    """Return meal recipes based on meal type."""
    meals = {
        "Breakfast": [
            {
                "Name": "Vegetable Upma",
                "Ingredients": "1 cup semolina, \n2 cups water, \n1 medium onion (finely chopped), \n1 medium tomato (chopped), \n1 carrot (finely chopped), \n1/2 cup green peas, \n2 green chilies (slit), \n1/2 tsp mustard seeds, \n1/2 tsp cumin seeds, \npinch of salt, \nfresh coriander leaves (for garnish)",
                "Instructions": "Roast semolina in a dry pan until golden brown, \nIn another pot, heat water and bring to a boil, \nIn a separate pan, dry roast mustard and cumin seeds, \nAdd chopped onions and green chilies, sauté until onions are translucent, \nAdd chopped tomatoes, carrots, and peas, cook until soft, \nAdd salt and roasted semolina, stir well, \nPour in boiling water, stir continuously to avoid lumps, \nCover and let it simmer for 5 minutes, \nGarnish with fresh coriander leaves before serving.",
                "Nutritional Info": "Calories: 300, Protein: 10g, Carbs: 55g, Fats: 2g"
            },
            {
                "Name": "Chickpea Pancakes",
                "Ingredients": "1 cup chickpea flour, 1 1/4 cups water, 1/2 tsp turmeric powder, 1/2 tsp cumin powder, 1/2 tsp red chili powder, pinch of salt, 1/4 cup finely chopped spinach, 1/4 cup finely chopped onion, lemon wedges (for serving)",
                "Instructions": "In a bowl, mix chickpea flour with water to form a smooth batter, \nAdd turmeric, cumin, red chili powder, and salt, mix well, \nFold in chopped spinach and onion, \nHeat a non-stick pan, pour a ladleful of batter, \nSpread it evenly and cook on medium heat until edges lift, \nFlip and cook the other side until golden, \nServe hot with lemon wedges.",
                "Nutritional Info": "Calories: 200, Protein: 15g, Carbs: 35g, Fats: 3g"
            },
            {
                "Name": "Masala Poha",
                "Ingredients": "2 cups flattened rice (poha), 1 medium onion (finely chopped), 1 medium potato (diced), 2 green chilies (slit), 1/2 tsp mustard seeds, 1/2 tsp turmeric powder, pinch of salt, 1/4 cup fresh coriander leaves (chopped), lemon juice (to taste)",
                "Instructions": "Rinse flattened rice under water and drain, \nIn a pan, heat water and cook diced potatoes until tender, \nIn a separate pan, dry roast mustard seeds, \nAdd chopped onions and green chilies, sauté until onions are translucent, \nAdd turmeric and salt, stir well, \nAdd the drained poha and cooked potatoes, mix gently, \nCook for 2-3 minutes, remove from heat, \nGarnish with coriander leaves and lemon juice before serving.",
                "Nutritional Info": "Calories: 250, Protein: 5g, Carbs: 48g, Fats: 1g"
            },
            {
                "Name": "Lentil Idli",
                "Ingredients": "1 cup split urad dal (soaked overnight), 1 cup rice (soaked overnight), 1/2 tsp salt, 1/2 tsp cumin seeds, 1/2 tsp black pepper, water (as needed)",
                "Instructions": "Blend soaked urad dal and rice into a smooth batter, \nAdd salt, cumin seeds, and black pepper, mix well, \nLet the batter ferment for 6-8 hours in a warm place, \nGrease idli molds, pour in the batter, \nSteam for 10-12 minutes or until cooked through, \nServe hot with coconut chutney or sambar.",
                "Nutritional Info": "Calories: 180, Protein: 10g, Carbs: 30g, Fats: 1g"
            },
            {
                "Name": "Aloo Paratha (without oil)",
                "Ingredients": "2 cups whole wheat flour, 2 medium potatoes (boiled and mashed), 1/2 tsp cumin seeds, 1/2 tsp garam masala, pinch of salt, water (as needed), fresh coriander leaves (for filling)",
                "Instructions": "In a bowl, mix whole wheat flour with water to form a dough, \nIn another bowl, mix mashed potatoes, cumin seeds, garam masala, salt, and coriander leaves, \nDivide the dough and potato filling into equal portions, \nRoll out a portion of dough, place a portion of filling in the center, \nSeal and roll out gently to form a flatbread, \nCook on a non-stick skillet until both sides are golden brown, \nServe hot with yogurt or pickles.",
                "Nutritional Info": "Calories: 320, Protein: 9g, Carbs: 55g, Fats: 2g"
            },
            {
                "Name": "Vegetable Dalia",
                "Ingredients": "1 cup broken wheat (dalia), 2 cups water, 1 medium onion (chopped), 1 carrot (chopped), 1/2 cup green peas, 1/2 tsp turmeric powder, pinch of salt, fresh coriander leaves (for garnish)",
                "Instructions": "Dry roast broken wheat in a pan until slightly golden, \nIn another pot, heat water and bring to a boil, \nIn a separate pan, sauté onions until translucent, \nAdd chopped carrots and green peas, cook until soft, \nAdd turmeric and salt, stir well, \nAdd roasted broken wheat and boiling water, mix well, \nCover and simmer until water is absorbed, \nGarnish with fresh coriander leaves before serving.",
                "Nutritional Info": "Calories: 250, Protein: 10g, Carbs: 45g, Fats: 2g"
            },
            {
                "Name": "Spinach and Chickpea Salad",
                "Ingredients": "1 cup boiled chickpeas, 1 cup fresh spinach leaves, 1/2 medium cucumber (chopped), 1 medium tomato (chopped), 1/4 cup red onion (finely chopped), lemon juice (to taste), salt (to taste), black pepper (to taste)",
                "Instructions": "In a bowl, combine boiled chickpeas, spinach, cucumber, tomato, and onion, \nDrizzle with lemon juice, add salt and black pepper to taste, \nToss everything gently until well mixed, \nServe chilled or at room temperature.",
                "Nutritional Info": "Calories: 200, Protein: 10g, Carbs: 30g, Fats: 2g"
            },
            {
                "Name": "Quinoa Porridge",
                "Ingredients": "1/2 cup quinoa, 2 cups water, 1/2 tsp cinnamon powder, pinch of salt, 1/2 banana (sliced), 1/4 cup chopped nuts (almonds or walnuts), honey (optional, for serving)",
                "Instructions": "Rinse quinoa under cold water, \nIn a pot, combine quinoa, water, cinnamon powder, and salt, \nBring to a boil, then reduce heat and simmer for 15 minutes, \nFluff with a fork and serve warm, \nTop with banana slices and chopped nuts, \nDrizzle with honey if desired.",
                "Nutritional Info": "Calories: 250, Protein: 8g, Carbs: 45g, Fats: 5g"
            },
            {
                "Name": "Fruit Chaat",
                "Ingredients": "1 cup mixed fruits (apple, banana, orange), 1/2 tsp chaat masala, 1/2 tsp lemon juice, pinch of salt",
                "Instructions": "Chop mixed fruits into small pieces, \nIn a bowl, combine chopped fruits, chaat masala, lemon juice, and salt, \nMix well until fruits are coated with spices, \nServe fresh as a nutritious breakfast option.",
                "Nutritional Info": "Calories: 150, Protein: 2g, Carbs: 35g, Fats: 0g"
            }
        ],

        "Lunch": [
            {
                "Name": "Chickpea Salad",
                "Ingredients": "1 cup boiled chickpeas, 1/2 cup chopped cucumber, 1/2 cup chopped tomatoes, 1/4 cup chopped onions, 1/4 cup chopped bell peppers, 2 tablespoons lemon juice, 1 teaspoon cumin powder, salt to taste",
                "Instructions": "In a large bowl, combine the boiled chickpeas, chopped cucumber, chopped tomatoes, chopped onions, and chopped bell peppers. \nAdd lemon juice, cumin powder, and salt. \nToss everything together until well mixed. \nServe chilled or at room temperature.",
                "Nutritional Info": "Calories: 250, Protein: 12g, Carbs: 40g, Fats: 4g"
            },
            {
                "Name": "Vegetable Biryani",
                "Ingredients": "1 cup basmati rice, 1/2 cup mixed vegetables (carrots, peas, beans), 1/2 onion sliced, 1 tomato chopped, 2 green chilies, 1 teaspoon ginger-garlic paste, 1 teaspoon cumin seeds, 1 teaspoon garam masala, 2 cups water, salt to taste",
                "Instructions": "Rinse the basmati rice until the water runs clear. \nSoak the rice in water for 30 minutes, then drain. \nIn a pot, heat water and add cumin seeds, sliced onion, ginger-garlic paste, and green chilies. \nSauté until onions are golden brown. \nAdd chopped tomatoes and mixed vegetables, cooking until soft. \nAdd the soaked rice and garam masala, mixing well. \nPour in the water and add salt. \nBring to a boil, then reduce heat, cover, and cook for 15 minutes or until rice is tender. \nFluff the biryani with a fork before serving.",
                "Nutritional Info": "Calories: 350, Protein: 8g, Carbs: 70g, Fats: 2g"
            },
            {
                "Name": "Lentil Soup",
                "Ingredients": "1 cup red lentils, 4 cups water, 1/2 onion chopped, 1 carrot chopped, 1 tomato chopped, 1 teaspoon turmeric powder, 1 teaspoon cumin powder, salt to taste, fresh coriander for garnish",
                "Instructions": "In a pot, combine red lentils, chopped onion, carrot, tomato, turmeric powder, cumin powder, and water. \nBring to a boil, then reduce heat and simmer for 25-30 minutes until lentils are soft. \nBlend the soup for a smoother texture, if desired. \nAdd salt to taste and garnish with fresh coriander before serving.",
                "Nutritional Info": "Calories: 220, Protein: 12g, Carbs: 36g, Fats: 1g"
            },
            {
                "Name": "Spinach and Potato Curry",
                "Ingredients": "2 cups fresh spinach, 2 medium potatoes diced, 1/2 onion chopped, 1 tomato chopped, 1 teaspoon cumin seeds, 1 teaspoon coriander powder, 1/2 teaspoon red chili powder, salt to taste",
                "Instructions": "In a pan, dry roast cumin seeds until fragrant. \nAdd chopped onions and sauté until golden. \nStir in diced potatoes, chopped tomato, coriander powder, red chili powder, and salt. \nCook for 5-7 minutes, adding a splash of water to prevent sticking. \nAdd fresh spinach and cover, cooking until spinach wilts and potatoes are tender.",
                "Nutritional Info": "Calories: 180, Protein: 5g, Carbs: 35g, Fats: 0g"
            },
            {
                "Name": "Quinoa and Vegetable Stir-Fry",
                "Ingredients": "1 cup cooked quinoa, 1/2 cup broccoli florets, 1/2 cup bell peppers sliced, 1/4 cup carrot julienned, 1/4 cup soy sauce (low sodium), 1 teaspoon sesame seeds",
                "Instructions": "In a large pan, heat the cooked quinoa over medium heat. \nAdd broccoli, bell peppers, and carrots, sautéing for 5-7 minutes until vegetables are tender. \nStir in soy sauce and sesame seeds, mixing well. \nCook for an additional 2-3 minutes, then serve warm.",
                "Nutritional Info": "Calories: 300, Protein: 10g, Carbs: 54g, Fats: 6g"
            },
            {
                "Name": "Stuffed Bell Peppers",
                "Ingredients": "4 bell peppers, 1 cup cooked brown rice, 1/2 cup black beans, 1/2 cup corn, 1 teaspoon cumin powder, 1 teaspoon paprika, salt to taste",
                "Instructions": "Preheat oven to 375°F (190°C). \nCut the tops off the bell peppers and remove seeds. \nIn a bowl, mix cooked brown rice, black beans, corn, cumin powder, paprika, and salt. \nStuff each bell pepper with the mixture and place them in a baking dish. \nBake for 25-30 minutes until the peppers are tender.",
                "Nutritional Info": "Calories: 220, Protein: 8g, Carbs: 42g, Fats: 1g"
            },
            {
                "Name": "Vegetable Khichdi",
                "Ingredients": "1 cup moong dal, 1 cup basmati rice, 1/2 cup mixed vegetables, 1/2 teaspoon turmeric powder, 1 teaspoon cumin seeds, salt to taste, 4 cups water",
                "Instructions": "Rinse moong dal and basmati rice. \nIn a pot, combine dal, rice, mixed vegetables, turmeric powder, cumin seeds, and water. \nBring to a boil, then reduce heat and simmer until everything is soft (about 25-30 minutes). \nStir occasionally and add water if needed. \nServe warm with a sprinkle of fresh coriander.",
                "Nutritional Info": "Calories: 320, Protein: 15g, Carbs: 60g, Fats: 1g"
            },
            {
                "Name": "Cabbage and Carrot Slaw",
                "Ingredients": "2 cups shredded cabbage, 1 cup shredded carrots, 1/4 cup chopped green onions, 2 tablespoons lemon juice, salt to taste, black pepper to taste",
                "Instructions": "In a large bowl, combine shredded cabbage, shredded carrots, and chopped green onions. \nDrizzle lemon juice over the vegetables and season with salt and black pepper. \nToss well until everything is coated. \nLet sit for 10 minutes before serving to allow flavors to meld.",
                "Nutritional Info": "Calories: 70, Protein: 2g, Carbs: 15g, Fats: 0g"
            },
            {
                "Name": "Dal Tadka",
                "Ingredients": "1 cup yellow split peas (toor dal), 4 cups water, 1/2 onion chopped, 1 tomato chopped, 1 teaspoon ginger-garlic paste, 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, 1 teaspoon coriander powder, salt to taste, fresh coriander for garnish",
                "Instructions": "Rinse the split peas and soak for 30 minutes. \nIn a pressure cooker, combine soaked dal, water, chopped onion, tomato, ginger-garlic paste, turmeric, and salt. \nCook for about 3-4 whistles or until the dal is soft. \nIn a separate pan, heat dry cumin seeds until fragrant, then pour over the cooked dal. \nMix well and garnish with fresh coriander before serving.",
                "Nutritional Info": "Calories: 240, Protein: 12g, Carbs: 45g, Fats: 1g"
            }
        ],
        "Dinner": [
            {
                "Name": "Vegetable Biryani",
                "Ingredients": "1 cup basmati rice, 2 cups water, 1 cup mixed vegetables (carrots, peas, beans), 1 onion (sliced), 2 tomatoes (chopped), 1 teaspoon cumin seeds, 1 teaspoon garam masala, 1 teaspoon turmeric powder, 1 teaspoon coriander powder, salt to taste, fresh coriander leaves (for garnish)",
                "Instructions": "1. Rinse the basmati rice under cold water until the water runs clear. \n2. Soak the rice in water for 30 minutes, then drain. \n3. In a large pot, heat water and add the cumin seeds. \n4. Once they start to sizzle, add the sliced onion and sauté until translucent. \n5. Add chopped tomatoes and cook until soft. \n6. Stir in the mixed vegetables, turmeric, coriander powder, and salt. \n7. Cook for 5 minutes until vegetables are tender. \n8. Add the soaked rice and gently mix. \n9. Pour in the 2 cups of water and bring to a boil. \n10. Reduce heat to low, cover, and cook for 15 minutes. \n11. Remove from heat and let it sit for 5 minutes before fluffing with a fork. \n12. Sprinkle garam masala and garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 250, Protein: 5g, Carbs: 52g, Fats: 1g"
            },
            {
                "Name": "Chickpea Curry",
                "Ingredients": "1 can chickpeas (400g), 1 onion (chopped), 2 tomatoes (chopped), 2 green chilies (slit), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, 1 teaspoon coriander powder, 1 teaspoon garam masala, salt to taste, fresh coriander leaves (for garnish)",
                "Instructions": "1. Drain and rinse the chickpeas. \n2. In a pan, heat water and add cumin seeds. \n3. Once they sizzle, add the chopped onion and sauté until golden. \n4. Add chopped tomatoes and green chilies, cooking until soft. \n5. Stir in turmeric, coriander powder, and salt. \n6. Add the chickpeas and mix well. \n7. Pour in a cup of water and bring to a boil. \n8. Reduce heat and simmer for 15-20 minutes. \n9. Stir in garam masala and cook for another 5 minutes. \n10. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 300, Protein: 15g, Carbs: 45g, Fats: 3g"
            },
            {
                "Name": "Palak Daal",
                "Ingredients": "1 cup split yellow lentils (moong dal), 2 cups spinach (chopped), 1 onion (chopped), 1 tomato (chopped), 2 green chilies (slit), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, salt to taste, fresh lemon juice (to taste), fresh coriander leaves (for garnish)",
                "Instructions": "1. Rinse the lentils under cold water. \n2. In a pot, boil 3 cups of water and add the lentils. \n3. Cook for about 20 minutes until soft, then add chopped spinach. \n4. In a separate pan, heat water and add cumin seeds. \n5. Add chopped onion and sauté until golden. \n6. Stir in chopped tomato, green chilies, turmeric, and salt. \n7. Cook until tomatoes are soft. \n8. Add the sautéed mixture to the cooked lentils and stir well. \n9. Simmer for 5 minutes, then add lemon juice. \n10. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 220, Protein: 12g, Carbs: 40g, Fats: 1g"
            },
            {
                "Name": "Aloo Gobi (Potato and Cauliflower)",
                "Ingredients": "2 medium potatoes (cubed), 1 small cauliflower (florets), 1 onion (sliced), 2 tomatoes (chopped), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, 1 teaspoon coriander powder, 1 teaspoon garam masala, salt to taste, fresh coriander leaves (for garnish)",
                "Instructions": "1. In a pan, heat water and add cumin seeds. \n2. Once they sizzle, add the sliced onion and sauté until golden. \n3. Add chopped tomatoes and cook until soft. \n4. Stir in turmeric, coriander powder, and salt. \n5. Add cubed potatoes and cauliflower florets. \n6. Mix well and cover to cook for 15 minutes on low heat, stirring occasionally. \n7. Once vegetables are tender, sprinkle garam masala and mix well. \n8. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 180, Protein: 4g, Carbs: 36g, Fats: 1g"
            },
            {
                "Name": "Mixed Vegetable Stir Fry",
                "Ingredients": "1 cup bell peppers (sliced), 1 cup broccoli (florets), 1 carrot (sliced), 1 onion (sliced), 2 cloves garlic (minced), 1 teaspoon ginger (grated), 1 teaspoon cumin seeds, salt to taste, fresh lemon juice (to taste), fresh coriander leaves (for garnish)",
                "Instructions": "1. In a pan, heat water and add cumin seeds. \n2. Once they start to sizzle, add minced garlic and grated ginger. \n3. Add sliced onion and sauté until translucent. \n4. Add sliced bell peppers, broccoli, and carrot. \n5. Stir-fry for 5-7 minutes until vegetables are tender yet crisp. \n6. Season with salt and a splash of lemon juice. \n7. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 120, Protein: 3g, Carbs: 25g, Fats: 0g"
            },
            {
                "Name": "Vegetable Khichdi",
                "Ingredients": "1 cup basmati rice, 1 cup split yellow lentils (moong dal), 2 cups mixed vegetables (carrots, peas, beans), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, salt to taste, fresh coriander leaves (for garnish)",
                "Instructions": "1. Rinse the rice and lentils under cold water. \n2. In a pressure cooker, heat water and add cumin seeds. \n3. Once they sizzle, add the rice and lentils, mixed vegetables, turmeric, and salt. \n4. Add 4 cups of water and stir well. \n5. Close the lid and cook for 3 whistles. \n6. Let the pressure release naturally, then open and fluff gently. \n7. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 300, Protein: 10g, Carbs: 55g, Fats: 1g"
            },
            {
                "Name": "Quinoa Pulao",
                "Ingredients": "1 cup quinoa, 2 cups water, 1 cup mixed vegetables (peas, carrots, beans), 1 onion (sliced), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, salt to taste, fresh coriander leaves (for garnish)",
                "Instructions": "1. Rinse the quinoa under cold water. \n2. In a pot, heat water and add cumin seeds. \n3. Once they start to sizzle, add the sliced onion and sauté until golden. \n4. Stir in mixed vegetables, turmeric, and salt. \n5. Add the rinsed quinoa and 2 cups of water. \n6. Bring to a boil, then reduce heat and cover. \n7. Cook for 15 minutes until quinoa is fluffy and water is absorbed. \n8. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 250, Protein: 8g, Carbs: 45g, Fats: 3g"
            },
            {
                "Name": "Lentil and Spinach Soup",
                "Ingredients": "1 cup red lentils, 2 cups spinach (chopped), 1 onion (chopped), 2 cloves garlic (minced), 1 teaspoon cumin seeds, 1 teaspoon turmeric powder, salt to taste, fresh lemon juice (to taste), fresh coriander leaves (for garnish)",
                "Instructions": "1. Rinse the lentils under cold water. \n2. In a pot, boil 3 cups of water and add the lentils. \n3. Cook for about 15 minutes until soft, then add chopped spinach. \n4. In a separate pan, heat water and add cumin seeds. \n5. Add minced garlic and chopped onion, sauté until golden. \n6. Stir in turmeric and salt. \n7. Add the sautéed mixture to the cooked lentils and stir well. \n8. Simmer for 5 more minutes. \n9. Add fresh lemon juice to taste. \n10. Garnish with fresh coriander leaves before serving.",
                "Nutritional_info": "Calories: 210, Protein: 12g, Carbs: 30g, Fats: 1g"
            },
        ],
        "Snacks": [
             {
                "Name": "Spicy Roasted Chickpeas",
                "Ingredients": "1 can (400g) chickpeas, drained and rinsed, \n1 tsp cumin powder, \n1 tsp coriander powder, \n1/2 tsp red chili powder, \n1/2 tsp turmeric powder, \n1/2 tsp salt, \n1/2 tsp black pepper, \n1/2 lemon, juiced",
                "Instructions": "Preheat the oven to 200°C (400°F), \nSpread the chickpeas on a baking sheet and pat dry with a paper towel, \nIn a bowl, mix the spices and lemon juice, \nAdd the chickpeas to the bowl and toss to coat, \nSpread the spiced chickpeas back on the baking sheet, \nRoast in the oven for 25-30 minutes until crispy, \nLet them cool before serving.",
                "Nutritional_info": "Calories: 120, Protein: 6g, Carbs: 18g, Fats: 2g"
            },
            {
                "Name": "Vegetable Bhel Puri",
                "Ingredients": "1 cup puffed rice, \n1/2 cup finely chopped cucumber, \n1/2 cup finely chopped tomatoes, \n1/2 cup finely chopped onion, \n1/4 cup finely chopped coriander leaves, \n1 green chili, finely chopped, \n1 tsp chaat masala, \n1/2 lemon, juiced, \nSalt to taste",
                "Instructions": "In a large mixing bowl, combine the puffed rice, cucumber, tomatoes, onion, coriander, and green chili, \nAdd chaat masala, lemon juice, and salt to taste, \nToss everything together until well mixed, \nServe immediately for best crunchiness.",
                "Nutritional_info": "Calories: 100, Protein: 3g, Carbs: 22g, Fats: 0g"
            },
            {
                "Name": "Masoor Dal Chaat",
                "Ingredients": "1 cup boiled masoor dal (red lentils), \n1/2 cup finely chopped onion, \n1/2 cup finely chopped tomatoes, \n1/4 cup chopped coriander leaves, \n1 green chili, finely chopped, \n1 tsp chaat masala, \n1/2 lemon, juiced, \nSalt to taste",
                "Instructions": "In a bowl, combine boiled masoor dal, onion, tomatoes, coriander, and green chili, \nSprinkle with chaat masala, lemon juice, and salt to taste, \nMix well until combined, \nServe chilled or at room temperature.",
                "Nutritional_info": "Calories: 150, Protein: 10g, Carbs: 25g, Fats: 1g"
            },
            {
                "Name": "Cucumber and Mint Salad",
                "Ingredients": "2 large cucumbers, diced, \n1/2 cup chopped fresh mint leaves, \n1/4 cup finely chopped onion, \n1/2 lemon, juiced, \nSalt to taste, \n1/2 tsp black pepper",
                "Instructions": "In a large bowl, combine the diced cucumbers, mint leaves, and onion, \nDrizzle with lemon juice, sprinkle salt and black pepper, \nMix gently to combine all ingredients, \nLet it sit for 10 minutes before serving to enhance flavors.",
                "Nutritional_info": "Calories: 50, Protein: 2g, Carbs: 12g, Fats: 0g"
            },
            {
                "Name": "Stuffed Bell Peppers with Quinoa",
                "Ingredients": "3 bell peppers, halved and seeds removed, \n1 cup cooked quinoa, \n1/2 cup finely chopped tomatoes, \n1/2 cup finely chopped onion, \n1/2 tsp cumin powder, \n1/2 tsp coriander powder, \nSalt to taste, \n1/2 lemon, juiced",
                "Instructions": "Preheat the oven to 180°C (350°F), \nIn a bowl, mix cooked quinoa, tomatoes, onion, cumin powder, coriander powder, salt, and lemon juice, \nStuff each bell pepper half with the quinoa mixture, \nPlace the stuffed peppers on a baking tray, \nBake in the oven for 25-30 minutes until the peppers are tender, \nServe warm.",
                "Nutritional_info": "Calories: 180, Protein: 6g, Carbs: 36g, Fats: 2g"
            },
        ],
    }

    return pd.DataFrame(meals.get(meal_type, []))
