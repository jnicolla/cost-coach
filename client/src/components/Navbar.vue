<template>
    <div>
        <md-tabs md-sync-route md-alignment="right" class="md-primary">
        
       
        <md-tab id="tab-about" md-label="About" to="/about"></md-tab>
        <md-tab id="tab-home" md-label="Cost Calculator" to="/"></md-tab>
        <md-tab id="tab-timeline" md-label="Timeline" to="/timeline"></md-tab>
         <md-tab id="tab-guide" md-label="Guide" to="/guide"></md-tab>
         <md-tab id="tab-Disclaimer" md-label="Disclaimer" to="/Disclaimer"></md-tab>
        </md-tabs>
    </div>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>
