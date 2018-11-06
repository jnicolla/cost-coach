<template>
  <v-toolbar color = "#d65f36" dark>
   
    <v-toolbar-title>Cost Coach</v-toolbar-title>
    <v-spacer></v-spacer>
    <div class="hidden-sm-and-down">
     
    <router-link to = "/Home">
              <v-btn flat>Home</v-btn>
      </router-link>


    <router-link to = "/CostCalculator">
             <v-btn flat>Cost Calculator</v-btn>
      </router-link>

     
      <router-link to = "/Timeline">
             <v-btn flat>Timeline</v-btn>
      </router-link>
      
       <router-link to = "/Guide">
             <v-btn flat>Conversation Guideline</v-btn>
      </router-link>

    <router-link to = "/Disclaimer">
             <v-btn flat>Disclaimer</v-btn>
      </router-link>




    </div>
  </v-toolbar>
</template>
