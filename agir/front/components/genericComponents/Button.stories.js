import React from "react";

import Button from "./Button";

export default {
  component: Button,
  title: "Button",
};

const Template = (args) => <Button {...args} />;

export const Default = Template.bind({});
Default.args = { small: false, disabled: false, children: "Texte du bouton" };

export const PrimaryColor = Template.bind({});
PrimaryColor.args = {
  ...Default.args,
  color: "primary",
};

export const SecondaryColor = Template.bind({});
SecondaryColor.args = {
  ...Default.args,
  color: "secondary",
};

export const Unavailable = Template.bind({});
Unavailable.args = { ...Default.args, color: "unavailable" };

export const SmallExample = Template.bind({});
SmallExample.args = { ...Default.args, small: true };

export const DisabledExample = Template.bind({});
DisabledExample.args = { ...Default.args, disabled: true };
