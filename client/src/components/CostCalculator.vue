<template>
<div id="app">
  <v-app id="inspire">
    <v-content>
          <v-stepper v-model="stepper">
        <v-stepper-header>
            
            <div class="step" v-for="(step, index) in steps" :key=index>
                <v-stepper-step color="#232859"
                    :edit-icon="'check'"
                    :complete-icon="'edit'"
                    :step="index + 1"
                    :complete="(index + 1 ) <= stepper"
                    :editable="(index + 1) < stepper">{{ step.label }}</v-stepper-step>
                <v-divider></v-divider>
            </div>
            
        </v-stepper-header>
        <v-stepper-items>
            <v-stepper-content step="1">
                <v-overflow-btn
            :items="dropdown_icon"
            label="Insurance Type"
            segmented
            color = "#232859"
          ></v-overflow-btn>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat @click.native="stepper = 1">Back</v-btn>
                    <v-btn color="#d65f36" dark @click.native="stepper = 2">Continue</v-btn>
                </v-card-actions>
            </v-stepper-content>
            <v-stepper-content step="2">
               <v-overflow-btn
            :items="dropdown_icon2"
            label="Diagnosis"
            segmented
            color = "#232859"
          ></v-overflow-btn>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat @click.native="stepper = 1">Back</v-btn>
                    <v-btn color="#d65f36" dark @click.native="stepper = 3">Continue</v-btn>
                </v-card-actions>
            </v-stepper-content>
            <v-stepper-content step="3">
               <v-overflow-btn
            :items="dropdown_icon3"
            label="Medication"
            segmented
            color = "#232859"
          ></v-overflow-btn>
              ––>  <v-card color="#232859" class="mb-5" height="200px"></v-card>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat @click.native="stepper = 2">Back</v-btn>
                    <v-btn color="#d65f36" dark @click.native="stepper = 1">Continue</v-btn>
                </v-card-actions>
            </v-stepper-content>
        </v-stepper-items>
  </v-stepper>
  <template>
  <div class="text-xs-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-btn
        slot="activator"
        color="red lighten-2"
        dark
      >
        What is this? Click here to learn more
      </v-btn>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          What is the cost calculator?
        </v-card-title>

        <v-card-text>
          This is the cost calculator. Please answer every question in this survey.
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
</template>

    </v-content>
  </v-app>
</div>
</template>



<script>
  export default 
{
  data: () => ({

      dialog: false,
     
                stepper: 0,
            steps: [
                {
                    label: 'Insurance',
                    completed: false,
                },
                {
                    label: 'Diagnosis',
                    completed: false,
                },
                {
                    label: 'Medication',
                    completed: false,
                },
            ],
            dropdown_icon: [
      { text: 'Duke Basic', callback: () => console.log('Duke Basic') },
      { text: 'Duke Select', callback: () => console.log('Duke Select') },
      { text: 'Duke Care', callback: () => console.log('Duke Care') },
      { text: 'Duke Option', callback: () => console.log('Duke Option') },
    ],
     dropdown_icon2: [
      { text: 'Prostate Cancer', callback: () => console.log('Prostate Cancer') }
     ],
     dropdown_icon3: [
      { text: 'Abiraterone', callback: () => console.log('Abiraterone') },
      { text: 'Docetaxel', callback: () => console.log('Docetaxel') }
     ],
   
  }),
   
}

</script>