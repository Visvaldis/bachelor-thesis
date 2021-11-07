<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Crack Logo"
          class="shrink mr-2"
          contain
          src="./assets/crack.png"
          transition="scale-transition"
          width="40"
        />
      <v-toolbar-title>Auto cracks classification</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

      
    </v-app-bar>

    <v-main>
      <MainPage/>
    </v-main>
  </v-app>
</template>

<script>
import MainPage from './components/MainPage';

export default {
  name: 'App',

  components: {
    MainPage,
  },

  data: () => ({
    //
  }),
};
</script>
