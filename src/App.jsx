import { RecipeListPage } from "./pages/RecipeListPage";
import { useState } from "react";
import { RecipePage } from "./pages/RecipePage";

export const App = () => {
  const [chosenRecipe, setChosenRecipe] = useState();

  return (
    <div className="app">
      {chosenRecipe ? (
        <RecipePage recipe={chosenRecipe} clickFn={setChosenRecipe} />
      ) : (
        <RecipeListPage clickFn={setChosenRecipe} />
      )}
    </div>
  );
};
