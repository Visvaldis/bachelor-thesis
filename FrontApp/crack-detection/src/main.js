import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRx from 'vue-rx'
// install vue-rx
import VuejsClipper from "vuejs-clipper/dist/vuejs-clipper.umd";
//https://vuejsexamples.com/vue-js-image-clipping-components-using-vue-rx/
import "vuejs-clipper/dist/vuejs-clipper.css";

Vue.use(VueRx);
Vue.use(VuejsClipper, {
  components: {
     clipperBasic: true,
     clipperPreview: true
  }
}) 
Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
