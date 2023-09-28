import { Center } from "@chakra-ui/react";
import { useState } from "react";
import { TextInput } from "./ui/TextInput";
import { data } from "../utils/data";
import { RecipeList } from "./RecipeList";

export const RecipeSearch = ({ clickFn }) => {
  const [searchField, setSearchField] = useState("");

  const handleChange = (event) => {
    setSearchField(event.target.value);
  };

  const recipeList = data.hits.map((recipe) => recipe.recipe);
  //const recipeLabel = recipeList.map((label) => label.label);
  //const recipeHealthLabels = recipeList.map((label) => label.healthLabels);

  const matchedRecipes = recipeList.filter((recipe) => {
    return recipe.label.toLowerCase().includes(searchField.toLowerCase());
  });

  // const matchedHealthLabels = recipeList.filter((recipe) =>
  //   recipe.healthLabels((healthLabel) =>
  //     healthLabel.toLowerCase().includes(searchField.toLowerCase())
  //   )
  // );
  console.log("Recipes");
  console.log(matchedRecipes); // shows recipes filtered by recipe label in searchbar
  // console.log("HealthLabels");
  // console.log(matchedHealthLabels); // shows recipes filtered by Healthlabel in searchbar
  //   console.log(searchField);
  //   console.log("recipeName");
  //   console.log(recipeLabel);
  // console.log("match");
  // console.log(matchedRecipes);
  //   console.log("healthlabel");
  //   console.log(recipeHealthLabels);
  //   console.log("testvar");
  //   console.log(testvar);
  return (
    <>
      <Center flexDir={"column"} gap={5}>
        <label>Search for recipe names:</label>
        <TextInput changeFn={handleChange} w={200} mb={8} />
        <RecipeList recipes={matchedRecipes} clickFn={clickFn} />
      </Center>
    </>
  );
};
