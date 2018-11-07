<template>
<div>
<center> <font color="white">.</font></center>
 <center> <font color="white">.</font></center>
 <p align = "left"><font color="#232859"> <h1 class="display-4">Your Timeline</h1></font></p>
 
  <div class="text-xs-left">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-btn
        slot="activator"
        color="#232859"
        dark
      >
        What is this? Click me to learn more
      </v-btn>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          What does this timeline show?
        </v-card-title>

        <v-card-text>
          This provides an estimate of your expected cost per each visit. It is a timeline of you visits until you reach your out of pocket maximum.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
            Ok, got it!
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  
  <v-timeline>
    
    <v-timeline-item
      color="deep purple darken-4"
      fill-dot
      right
    >
    
      <v-card>
        <v-card-title class="deep purple darken-4">
          <v-icon
          color = "#ffa345"
            dark
            size="42"
            class="mr-3"
          >
            mdi-magnify
          </v-icon>
          <h2 class="display-1 white--text font-weight-light">Visit 1: Doctor Consultation</h2>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex xs10>
              Some Medical Information 
               <br>Cost: $450</br>
            </v-flex>
            <v-flex xs2>
              <v-icon size="64">mdi-calendar-text</v-icon>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="amber darken-4"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="amber darken-4 justify-end">
          <h2 class="display-1 mr-3 white--text font-weight-light">Visit 2: Chemotherapy Session</h2>
          <v-icon
            dark
            size="42"
            color = "#ffa345"
          >mdi-home-outline</v-icon>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex xs8>
            </v-flex>
            <v-flex xs4>
             Some Medical Information 
               <br>Cost: $350</br>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="deep purple darken-4"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="deep purple darken-4">
          <v-icon
            class="mr-3"
            dark
            size="42"
          >
            mdi-email-outline
          </v-icon>
          <h2 class="display-1 white--text font-weight-light">Visit 3: Doctor Visit</h2>
        </v-card-title>
        <v-container>
          <v-layout>
             <v-flex xs4>
             Some Medical Information 
               <br>Cost: $250</br>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="amber darken-4"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="amber darken-4 justify-end">
          <h2 class="display-1 mr-3 white--text font-weight-light">Visit 4: Chemotherapy Session</h2>
          <v-icon
            dark
            size="42"
          >
            mdi-account-multiple-outline
          </v-icon>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex xs2>
              <v-icon size="64">mdi-server-network</v-icon>
            </v-flex>
            <v-flex xs10>
               Some Medical Information 
               <br>Cost: $550</br>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="green accent-3"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="green accent-31">
          <v-icon
            class="mr-3"
            dark
            size="42"
          >
            mdi-phone-in-talk
          </v-icon>
          <h2 class="display-1 white--text font-weight-light">Visit 5: Pharmacy Visit; OOP REACHED!</h2>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex>
             Some Medical Information 
               <br>Cost: $150</br>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>
  </v-timeline>
  </div>
</template>


<script>

export default 
{
  data: () => ({
 
 
        dialog: false
}),
}
</script>