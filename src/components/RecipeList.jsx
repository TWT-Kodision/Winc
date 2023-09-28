import { RecipeCard } from "../components/RecipeCard";
import { Grid } from "@chakra-ui/react";

export const RecipeList = ({ recipes, clickFn }) => {
  // You can play around with the console log, but ultimately remove it once you are done
  // console.log(recipes.hits[0].recipe.label);

  return (
    <>
      <Grid templateColumns="repeat(3, 1fr)" gap={6}>
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.label} recipe={recipe} clickFn={clickFn} />
        ))}
      </Grid>
    </>
  );
};
