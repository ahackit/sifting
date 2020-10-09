# sifting-frontend

Frontend for Sifting through all the recipes I find.

## Use Case

Trying to find recipes on the internet and keeping track of them all sucks. I don't want to use a pre-built tool because of all the noise.
I also want to be able to easily select and prepare grocery lists.

## Features

List view of my recipes.
Clicking on a recipe goes to a detail view where I can find the steps required to complete the recipe. A picture. Ingredients required. Possible notes of issues I find with the recipe.
Admin pages to add recipes.
An ability to search recipes.
A way of generating grocery lists and sending a text to me.

## Who will use the application?

Me.

## Initial Install for this app?

npx create-nuxt-app my_app
npm install @storybook/vue babel-preset-vue
npm run generate
aws s3 cp dist s3://sifting-frontend --recursive

## How to stand up the application?

npm run dev
