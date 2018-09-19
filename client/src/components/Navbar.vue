<template>
    <div>
        <md-tabs md-sync-route md-alignment="right" class="md-primary">
        <md-tab id="tab-home" md-label="Home" to="/"></md-tab>
        <md-tab id="tab-guide" md-label="Guide" to="/guide"></md-tab>
        <md-tab id="tab-about" md-label="About" to="/about"></md-tab>
        </md-tabs>
    </div>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>
