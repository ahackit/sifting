import '../assets/css/tailwind.css'

import { storiesOf } from '@storybook/vue'
import RecipeCard from '../components/RecipeCard.vue'
storiesOf('RecipeCard', module)
  .add('As a component', () => ({
    components: { RecipeCard },
    template: '<RecipeCard />'
  }))
  .add("I don't work", () => '<RecipeCard />')
