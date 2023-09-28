import {
  Center,
  Image,
  Text,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
} from "@chakra-ui/react";

export const RecipeCard = ({ recipe, clickFn }) => {
  console.log();

  return (
    <ul>
      <Card
        gap={8}
        align="center"
        cursor={"pointer"}
        bg={"green.200"}
        onClick={() => clickFn(recipe)}
      >
        <CardHeader size="md">
          <Image src={recipe.image} borderRadius="lg" boxSize="md" />
          <Text align="center" fontSize="2xl" color="tomato">
            {recipe.label}
          </Text>
        </CardHeader>
        <CardBody>
          {recipe.healthLabels.includes("Vegan") ? ( // if vegan show "vegan"
            <Text>Vegan</Text>
          ) : recipe.healthLabels.includes("Vegetarian") ? ( // elif vegetarian show "vegetarian" else print nothing
            <Text>Vegetarian</Text>
          ) : null}
          <Text>Diet: {recipe.dietLabels + " "}</Text>
          <Text>Cautions: {recipe.cautions} </Text>
          <Text>Type: {recipe.mealType}</Text>
          <Text>Dish: {recipe.dishType}</Text>
        </CardBody>
      </Card>
    </ul>
  );
};
