<template>
<div>
  <v-app>
    <v-content>
      <v-container fluid>
        
        
        <v-stepper v-model="stepNo">
          
          
          <v-stepper-header>
            <div v-for="(step,index) in steps" :key=index>
              <v-stepper-step
                :edit-icon="'check'"
                :complete-icon="'edit'"
                :step="index + 1"
                :complete="(index+1)<=stepNo"
                :editable="(index+1)<stepNo"
              >
                {{step.label}}
              </v-stepper-step>
            </div>
            <!-- need to fix icons -->
            <v-stepper-step
              :edit-icon="'assignment'"
              :complete-icon="'assignment'"
              :step="4"
            >
              Results
            </v-stepper-step>
          </v-stepper-header>



          <v-stepper-items>
            
            <v-stepper-content step="1" height="400px">
                <v-select
                  :items="insurancePlans"
                  v-model="input.insurance"
                  label="Insurance"
                  hint="Select your insurance plan from the dropdown"
                  persistent-hint
                >
                </v-select>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn v-if="input.insurance" color="primary" @click.native="stepNo = 2">Continue</v-btn>
                    <v-btn v-else disabled color="primary" @click.native="stepNo = 2">Continue</v-btn>
                </v-card-actions>
            
            </v-stepper-content>

            <v-stepper-content step="2">
                <v-select
                    :items="diagnoses"
                    v-model="input.diagnosis"
                    label="Diagnosis"
                    hint="Select your diagnosis"
                    persistent-hint
                >
                </v-select>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat @click.native="stepNo = 1">Back</v-btn>
                    <v-btn v-if="input.diagnosis" color="primary" @click.native="stepNo = 3">Continue</v-btn>
                    <v-btn v-else disabled color="primary" @click.native="stepNo = 3">Continue</v-btn>
                </v-card-actions>
            </v-stepper-content>
            
            <v-stepper-content step="3">
                <v-select
                    :items="medications"
                    v-model="input.medications"
                    label="Medications"
                    hint="Select your medications"
                    persistent-hint
                    multiple
                >
                </v-select>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn flat @click.native="stepNo = 2">Back</v-btn>
                    <v-btn v-if="allInputs" color="success" @click.native="submit">Submit</v-btn>
                    <v-btn v-else disabled color="success" @click.native="submit">Submit</v-btn>
                </v-card-actions>
            </v-stepper-content>
            
            <v-stepper-content step="4">
              <div class="text-xs-center">
                <v-progress-circular v-if="loading" :size="100" color="primary" indeterminate></v-progress-circular>
                <div v-else>
                  <Timeline :data="tlData"></Timeline>
                </div>
              </div>
            </v-stepper-content>

          </v-stepper-items>
        
        
        </v-stepper>
      
      
      </v-container>
    </v-content>
  </v-app>
</div>
</template>



<script>
import axios from "axios";
import Timeline from './Timeline'

export default {

  data() {
    return {
      stepNo: 0,

      steps: [
        {
          label: "Insurance"
        },
        {
          label: "Diagnosis"
        },
        {
          label: "Medications"
        }
      ],

      insurancePlans: ["Duke Basic", "Duke Select","Duke Care","Duke Option"],

      diagnoses: ["Prostate Cancer"],

      medications: ["Abiraterone","Docetaxel"],

      input: {
        insurance: "",
        diagnosis: "",
        medications: []
      },

      loading: true,

      tlData: {}
    }
  },

  components: {
    Timeline
  },

  computed: {
    allInputs() {
      return this.input.insurance && this.input.diagnosis && this.input.medications.length;
    }
  },

  methods: {
    submit() {
      this.stepNo = 4;
      this.loading = true;
      const path = "https://costcoachserver.herokuapp.com/test";
      console.log(path);
      axios.post(path, this.input).then((res) => {
        this.tlData = res.data;
        this.loading = false;
      }).catch((err) => {
        console.log(err);
      });
    }
  }
}
</script>