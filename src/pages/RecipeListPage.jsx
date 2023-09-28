import { Center, Heading } from "@chakra-ui/react";
import { RecipeSearch } from "../components/RecipeSearch";

export const RecipeListPage = ({ clickFn }) => {
  // You can play around with the console log, but ultimately remove it once you are done
  //console.log(data.hits[0].recipe.label);

  return (
    <>
      <Center h="20vh" flexDir="column">
        <Heading>The Recipe App</Heading>
      </Center>
      <RecipeSearch clickFn={clickFn} />
    </>
  );
};
