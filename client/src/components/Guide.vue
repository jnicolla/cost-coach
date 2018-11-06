<template>

  <v-card flat>
    <v-card-text>
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
        How do I use this? Click me to learn more
      </v-btn>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          How to use the conversational guide
        </v-card-title>

        <v-card-text>
          Check the boxes that you are interested in
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="dialog = false"
          >
            Ok, Got it!
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs12 sm4 md4>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red darken-3"
              value="red darken-3"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red darken-3"
              value="red darken-3"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red darken-3"
              value="red darken-3"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red darken-3"
              value="red darken-3"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="red"
              value="red"
              hide-details
            ></v-checkbox>
           
          </v-flex>
          <v-flex xs12 sm4 md4>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo"
              value="indigo"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo darken-3"
              value="indigo darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo"
              value="indigo"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo darken-3"
              value="indigo darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo"
              value="indigo"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo darken-3"
              value="indigo darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo"
              value="indigo"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo darken-3"
              value="indigo darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo"
              value="indigo"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="indigo darken-3"
              value="indigo darken-3"
              hide-details
            ></v-checkbox>
          
          </v-flex>
          <v-flex xs12 sm4 md4>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange"
              value="orange"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange darken-3"
              value="orange darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange"
              value="orange"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange darken-3"
              value="orange darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange"
              value="orange"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange darken-3"
              value="orange darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange"
              value="orange"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange darken-3"
              value="orange darken-3"
              hide-details
            ></v-checkbox>
             <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange"
              value="orange"
              hide-details
            ></v-checkbox>
            <v-checkbox
              v-model="ex4"
              label="Question"
              color="orange darken-3"
              value="orange darken-3"
              hide-details
            ></v-checkbox>
            
          </v-flex>
        </v-layout>
      </v-container>
       <v-btn round color="#d65f36" dark>Create PDF</v-btn>

       
    
    </v-card-text>

  </v-card>
  
</template>

<script>

export default 
{
  data: () => ({
 
 
        dialog: false
}),
}
</script>