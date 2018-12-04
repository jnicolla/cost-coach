<template>
  <v-toolbar color="#232859" dark>
    <v-toolbar-side-icon to="/">
      <img src="../assets/favicon.png" height="30px">
    </v-toolbar-side-icon>
    <v-toolbar-title class="ml-0">CostCoach</v-toolbar-title>
    <v-spacer></v-spacer>
    <div class="hidden-sm-and-down">
      <router-link v-for="(link,index) in links" :key="index" :to="link.href">
        <v-btn flat>{{ link.label }}</v-btn>
      </router-link>
    </div>

    <v-menu class="hidden-md-and-up" offset-y>
      <v-btn slot="activator" icon>
        <v-icon>menu</v-icon>
      </v-btn>
      <v-list>
        <v-list-tile v-for="(link,index) in links"
          :key="index"
          :to="link.href"
          @click=""
        >
          <v-list-tile-title>{{ link.label }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>

<script>
export default {
  name: "Navbar",

  data() {
    return {
      links: [
        {
          label: "Home",
          href: "/"
        },
        {
          label: "Calculator",
          href: "/calculator"
        },
        {
          label: "Guide",
          href: "/guide"
        },
        {
          label: "Disclaimer",
          href: "/disclaimer"
        },
        {
          label: "About",
          href: "/about"
        }
      ]
    }
  }
}
</script>

<style>
a {
 text-decoration: none;
}
</style>
