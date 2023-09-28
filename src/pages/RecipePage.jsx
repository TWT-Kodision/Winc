import { Center, Image, Text, Heading } from "@chakra-ui/react";

export const RecipePage = ({ recipe, clickFn }) => {
  return (
    <ul>
      <div cursor={"pointer"} onClick={() => clickFn()}>
        <Heading>{recipe.label}</Heading>
        <Image src={recipe.image} height={200} width={200} />
        <Text>{recipe.mealType}</Text>
        <Text>{recipe.dishType}</Text>
        <Text>{recipe.totalTime}</Text>
        <Text>{recipe.dietLabels}</Text>
        <Text>{recipe.healthLabels}</Text>
        <Text>{recipe.cautions}</Text>
        {recipe.ingredients.map((ingredient, index) => (
          <Text key={index}>{ingredient.food}</Text>
        ))}
        <Text>{recipe.yield}</Text>
        <Text>
          {recipe.totalNutrients.ENERC_KCAL.label}:{" "}
          {recipe.totalNutrients.ENERC_KCAL.quantity}{" "}
          {recipe.totalNutrients.ENERC_KCAL.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.PROCNT.label}:{" "}
          {recipe.totalNutrients.PROCNT.quantity}{" "}
          {recipe.totalNutrients.PROCNT.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.PROCNT.label}:{" "}
          {recipe.totalNutrients.PROCNT.quantity}{" "}
          {recipe.totalNutrients.PROCNT.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.FAT.label}:{" "}
          {recipe.totalNutrients.FAT.quantity} {recipe.totalNutrients.FAT.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.CHOCDF.label}:{" "}
          {recipe.totalNutrients.CHOCDF.quantity}{" "}
          {recipe.totalNutrients.CHOCDF.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.CHOLE.label}:{" "}
          {recipe.totalNutrients.CHOLE.quantity}{" "}
          {recipe.totalNutrients.CHOLE.unit}{" "}
        </Text>
        <Text>
          {recipe.totalNutrients.NA.label}: {recipe.totalNutrients.NA.quantity}{" "}
          {recipe.totalNutrients.NA.unit}{" "}
        </Text>
      </div>
    </ul>
  );
};

// //
// Recipe name

// A picture of the recipe/meal

// Meal type

// Dish type

// Total cooking time

// Diet label

// All health labels

// Cautions

// Ingredients

// Servings

// Total nutrients (Energy in kcal, protein, fat, carbs, cholesterol, sodium)
