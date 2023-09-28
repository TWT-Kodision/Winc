import { Input } from "@chakra-ui/react";

export const TextInput = ({ changeFn, ...props }) => {
  return <Input className="input" onChange={changeFn} {...props}></Input>;
};
