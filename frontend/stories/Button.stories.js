import '../assets/css/tailwind.css'

import { storiesOf } from '@storybook/vue'
import Button from '../components/Button.vue'
storiesOf('Button', module)
  .add('As a component', () => ({
    components: { Button },
    template: '<Button />'
  }))
  .add("I don't work", () => '<Button />')
