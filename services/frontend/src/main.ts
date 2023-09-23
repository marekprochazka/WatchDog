import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import HelloWorld from './components/HelloWorld.vue'
import NotFound from './components/NotFound.vue'
import UsersList from './components/UsersList.vue';

// @ts-ignore
const componentName: string = django_component_name
// @ts-ignore
const props: object = django_component_props

console.log(componentName)
console.log(props)

const components = {
    hello: HelloWorld,
    users: UsersList
}
// @ts-ignore
const app = createApp(components[componentName] ?? NotFound, props)

app.use(createPinia())

app.mount('#app')
