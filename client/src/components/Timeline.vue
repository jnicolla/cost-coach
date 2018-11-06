<template>


  <v-timeline>
     <div class="text-xs-left">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-btn
        slot="activator"
        color="red lighten-2"
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
    <v-timeline-item
      color="#232859"
      fill-dot
      right
    >
    
      <v-card>
        <v-card-title class="purple lighten-2">
          <v-icon
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
              $100
            </v-flex>
            <v-flex xs2>
              <v-icon size="64">mdi-calendar-text</v-icon>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="amber lighten-1"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="amber lighten-1 justify-end">
          <h2 class="display-1 mr-3 white--text font-weight-light">Visit 2: Chemotherapy Session</h2>
          <v-icon
            dark
            size="42"
          >mdi-home-outline</v-icon>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex xs8>
              $35
            </v-flex>
            <v-flex xs4>
              Medication
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="cyan lighten-1"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="cyan lighten-1">
          <v-icon
            class="mr-3"
            dark
            size="42"
          >
            mdi-email-outline
          </v-icon>
          <h2 class="display-1 white--text font-weight-light">Doctor Visit</h2>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex
              v-for="n in 3"
              :key="n"
              xs4
            >
              $400
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="red lighten-1"
      fill-dot
      left
      small
    >
      <v-card>
        <v-card-title class="red lighten-1 justify-end">
          <h2 class="display-1 mr-3 white--text font-weight-light">Chemotherapy Session</h2>
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
               $300
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      color="green lighten-1"
      fill-dot
      right
    >
      <v-card>
        <v-card-title class="green lighten-1">
          <v-icon
            class="mr-3"
            dark
            size="42"
          >
            mdi-phone-in-talk
          </v-icon>
          <h2 class="display-1 white--text font-weight-light">Pharmacy Visit</h2>
        </v-card-title>
        <v-container>
          <v-layout>
            <v-flex>
              $25
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>


<script>

export default 
{
  data: () => ({
 
 
        dialog: false
}),
}
</script>