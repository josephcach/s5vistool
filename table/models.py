"""
@author: jcachaldora
models.py - defines Spectrum object 
"""
from django.db import models

class Spectrum(models.Model):
    #Columns in order of fits file    
    absdev_1700d = models.FloatField(blank=True, null = True)
    alpha1 = models.FloatField(blank=True, null = True)
    alpha16 = models.FloatField(blank=True, null = True)
    alpha50 = models.FloatField(blank=True, null = True)
    alpha84 = models.FloatField(blank=True, null = True)
    alpha99 = models.FloatField(blank=True, null = True)
    alpha_kurt = models.FloatField(blank=True, null = True)
    alpha_skew = models.FloatField(blank=True, null = True)
    alpha_std = models.FloatField(blank=True, null = True)
    chisq_1700d = models.FloatField(blank=True, null = True)
    comment = models.CharField(max_length=200,blank=True, null = True)
    dec = models.FloatField(blank=True, null = True)
    feh1 = models.FloatField(blank=True, null = True)
    feh16 = models.FloatField(blank=True, null = True)
    feh50 = models.FloatField(blank=True, null = True)
    feh84 = models.FloatField(blank=True, null = True)
    feh99 = models.FloatField(blank=True, null = True)
    feh_kurt = models.FloatField(blank=True, null = True)
    feh_skew = models.FloatField(blank=True, null = True)
    feh_std = models.FloatField(blank=True, null = True)
    field = models.CharField(max_length=50,blank=True, null = True)
    fig_name = models.CharField(max_length=100,blank=True, null = True)
    fileinfo = models.CharField(max_length=100,blank=True, null = True)
    logg1 = models.FloatField(blank=True, null = True)
    logg16 = models.FloatField(blank=True, null = True)
    logg50 = models.FloatField(blank=True, null = True)
    logg84 = models.FloatField(blank=True, null = True)
    logg99 = models.FloatField(blank=True, null = True)
    logg_kurt = models.FloatField(blank=True, null = True)
    logg_skew = models.FloatField(blank=True, null = True)
    logg_std = models.FloatField(blank=True, null = True)
    name = models.CharField(max_length=50,blank=True, null = True)
    ra = models.FloatField(blank=True, null = True)
    redchisq_1700d = models.FloatField(blank=True, null = True)
    sn_1700d = models.FloatField(blank=True, null = True)
    teff1 = models.FloatField(blank=True, null = True)
    teff16 = models.FloatField(blank=True, null = True)
    teff50 = models.FloatField(blank=True, null = True)
    teff84 = models.FloatField(blank=True, null = True)
    teff99 = models.FloatField(blank=True, null = True)
    teff_kurt = models.FloatField(blank=True, null = True)
    teff_skew = models.FloatField(blank=True, null = True)
    teff_std = models.FloatField(blank=True, null = True)
    utend = models.CharField(max_length=20, blank=True, null = True)
    utmjd = models.FloatField(blank=True, null = True)
    utstart = models.CharField(max_length=20,blank=True, null = True)
    vel1 = models.FloatField(blank=True, null = True)
    vel16 = models.FloatField(blank=True, null = True)
    vel50 = models.FloatField(blank=True, null = True)
    vel84 = models.FloatField(blank=True, null = True)
    vel99 = models.FloatField(blank=True, null = True)
    vel_kurt = models.FloatField(blank=True, null = True)
    vel_skew = models.FloatField(blank=True, null = True)
    vel_std = models.FloatField(blank=True, null = True)
    fname = models.CharField(max_length=50,blank=True, null = True)
    gaia_source_id = models.CharField(max_length=50,blank=True, null = True)
    phot_bp_rp_excess_factor = models.FloatField(blank=True, null = True)
    parallax = models.FloatField(blank=True, null = True)
    parallax_error = models.FloatField(blank=True, null = True)
    phot_g_mean_mag = models.FloatField(blank=True, null = True)
    source_id = models.CharField(max_length=50,blank=True, null = True)
    pmra = models.FloatField(blank=True, null = True)
    pmdec = models.FloatField(blank=True, null = True)
    pmra_error = models.FloatField(blank=True, null = True)
    pmdec_error = models.FloatField(blank=True, null = True)
    pmra_pmdec_corr = models.FloatField(blank=True, null = True)
    phot_bp_mean_mag = models.FloatField(blank=True, null = True)
    phot_rp_mean_mag = models.FloatField(blank=True, null = True)
    ebv = models.FloatField(blank=True, null = True)
    flux_w1 = models.FloatField(blank=True, null = True)
    flux_w2 = models.FloatField(blank=True, null = True)
    dflux_w1 = models.FloatField(blank=True, null = True)
    dflux_w2 = models.FloatField(blank=True, null = True)
    j_2mass = models.FloatField(blank=True, null = True)
    h_2mass = models.FloatField(blank=True, null = True)
    k_2mass = models.FloatField(blank=True, null = True)
    u_skm = models.FloatField(blank=True, null = True)
    e_u_skm = models.FloatField(blank=True, null = True)
    v_skm = models.FloatField(blank=True, null = True)
    e_v_skm = models.FloatField(blank=True, null = True)
    g_skm = models.FloatField(blank=True, null = True)
    e_g_skm = models.FloatField(blank=True, null = True)
    r_skm = models.FloatField(blank=True, null = True)
    e_r_skm = models.FloatField(blank=True, null = True)
    i_skm = models.FloatField(blank=True, null = True)
    e_i_skm = models.FloatField(blank=True, null = True)
    z_skm = models.FloatField(blank=True, null = True)
    e_z_skm = models.FloatField(blank=True, null = True)
    starhorse_dist05 = models.FloatField(blank=True, null = True)
    starhorse_dist16 = models.FloatField(blank=True, null = True)
    starhorse_dist50 = models.FloatField(blank=True, null = True)
    starhorse_dist84 = models.FloatField(blank=True, null = True)
    starhorse_dist95 = models.FloatField(blank=True, null = True)
    decam_g = models.FloatField(blank=True, null = True)
    decam_r = models.FloatField(blank=True, null = True)
    decam_i = models.FloatField(blank=True, null = True)
    decam_z = models.FloatField(blank=True, null = True)
    decam_phot_src_bits = models.IntegerField(blank=True, null = True)
    qso_flag_wise = models.IntegerField(blank=True, null = True)
    priority = models.IntegerField(blank=True, null = True)
    primary = models.BooleanField(blank=True, null = True)
    moon_phase = models.FloatField(blank=True, null = True)
    moon_alt = models.FloatField(blank=True, null = True)
    moon_dist = models.FloatField(blank=True, null = True)
    good_star_pb = models.FloatField(blank=True, null = True)
    good_star = models.BooleanField(blank=True, null = True)
    vel_calib = models.FloatField(blank=True, null = True)
    vel_calib_std = models.FloatField(blank=True, null = True)
    feh_calib_std = models.FloatField(blank=True, null = True)
    
    def __str__(self):
        return str(self.source_id)
    """
    def generatesmallDB(cls, tbl):
        for i in range(0,44069):
            s=cls(ra=tbl['ra'][i], dec=tbl['dec'][i],vel_calib=tbl['vel_calib'][i],
            vel_calib_std=tbl['vel_calib_std'][i],feh50=tbl['feh50'][i],
            logg50=tbl['logg50'][i], teff50=tbl['teff50'][i],
            sn_1700d=tbl['sn_1700d'][i],utmjd=tbl['utmjd'][i],parallax=tbl['parallax'][i],
            phot_g_mean_mag=tbl['phot_g_mean_mag'][i],pmra=tbl['pmra'][i],
            pmdec=tbl['pmdec'][i],starhorse_dist50=tbl['starhorse_dist50'][i],
            decam_g=tbl['decam_g'][i],decam_r=tbl['decam_r'][i],
            priority=tbl['priority'][i],qso_flag_wise=tbl['qso_flag_wise'][i],
            primary=tbl['primary'][i],good_star_pb=tbl['good_star_pb'][i],
            good_star=tbl['good_star'][i])
            s.save()
        return
    """
    
    #Generate database with astropy table 'tbl'
    def generateDB(cls, tbl):
        #Test with len()
        for i in range(0, 44069):
            s=cls(absdev_1700d = tbl['absdev_1700d'][i],
            alpha1 = tbl['alpha1'][i],
            alpha16 = tbl['alpha16'][i],
            alpha50 = tbl['alpha50'][i],
            alpha84 = tbl['alpha84'][i],
            alpha99 = tbl['alpha99'][i],
            alpha_kurt = tbl['alpha_kurt'][i],
            alpha_skew = tbl['alpha_skew'][i],
            alpha_std = tbl['alpha_std'][i],
            chisq_1700d = tbl['chisq_1700d'][i],
            comment = tbl['comment'][i],
            dec = tbl['dec'][i],
            feh1 = tbl['feh1'][i],
            feh16 = tbl['feh16'][i],
            feh50 = tbl['feh50'][i],
            feh84 = tbl['feh84'][i],
            feh99 = tbl['feh99'][i],
            feh_kurt = tbl['feh_kurt'][i],
            feh_skew = tbl['feh_skew'][i],
            feh_std = tbl['feh_std'][i],
            field = tbl['field'][i],
            fig_name = tbl['fig_name'][i],
            fileinfo = tbl['fileinfo'][i],
            logg1 = tbl['logg1'][i],
            logg16 = tbl['logg16'][i],
            logg50 = tbl['logg50'][i],
            logg84 = tbl['logg84'][i],
            logg99 = tbl['logg99'][i],
            logg_kurt = tbl['logg_kurt'][i],
            logg_skew = tbl['logg_skew'][i],
            logg_std = tbl['logg_std'][i],
            name = tbl['name'][i],
            ra = tbl['ra'][i],
            redchisq_1700d = tbl['redchisq_1700d'][i],
            sn_1700d = tbl['sn_1700d'][i],
            teff1 = tbl['teff1'][i],
            teff16 = tbl['teff16'][i],
            teff50 = tbl['teff50'][i],
            teff84 = tbl['teff84'][i],
            teff99 = tbl['teff99'][i],
            teff_kurt = tbl['teff_kurt'][i],
            teff_skew = tbl['teff_skew'][i],
            teff_std = tbl['teff_std'][i],
            utend = tbl['utend'][i],
            utmjd = tbl['utmjd'][i],
            utstart = tbl['utstart'][i],
            vel1 = tbl['vel1'][i],
            vel16 = tbl['vel16'][i],
            vel50 = tbl['vel50'][i],
            vel84 = tbl['vel84'][i],
            vel99 = tbl['vel99'][i],
            vel_kurt = tbl['vel_kurt'][i],
            vel_skew = tbl['vel_skew'][i],
            vel_std = tbl['vel_std'][i],
            fname = tbl['name'][i],
            gaia_source_id = tbl['gaia_source_id'][i],
            phot_bp_rp_excess_factor = tbl['phot_bp_rp_excess_factor'][i],
            parallax = tbl['parallax'][i],
            parallax_error = tbl['parallax_error'][i],
            phot_g_mean_mag = tbl['phot_g_mean_mag'][i],
            source_id = tbl['source_id'][i],
            pmra = tbl['pmra'][i],
            pmdec = tbl['pmdec'][i],
            pmra_error = tbl['pmra_error'][i],
            pmdec_error = tbl['pmdec_error'][i],
            pmra_pmdec_corr = tbl['pmra_pmdec_corr'][i],
            phot_bp_mean_mag = tbl['phot_bp_mean_mag'][i],
            phot_rp_mean_mag = tbl['phot_rp_mean_mag'][i],
            ebv = tbl['ebv'][i],
            flux_w1 = tbl['flux_w1'][i],
            flux_w2 = tbl['flux_w2'][i],
            dflux_w1 = tbl['dflux_w1'][i],
            dflux_w2 = tbl['dflux_w2'][i],
            j_2mass = tbl['j_2mass'][i],
            h_2mass = tbl['h_2mass'][i],
            k_2mass = tbl['k_2mass'][i],
            u_skm = tbl['u_skm'][i],
            e_u_skm = tbl['e_u_skm'][i],
            v_skm = tbl['v_skm'][i],
            e_v_skm = tbl['e_v_skm'][i],
            g_skm = tbl['g_skm'][i],
            e_g_skm = tbl['e_g_skm'][i],
            r_skm = tbl['r_skm'][i],
            e_r_skm = tbl['e_r_skm'][i],
            i_skm = tbl['i_skm'][i],
            e_i_skm = tbl['e_i_skm'][i],
            z_skm = tbl['z_skm'][i],
            e_z_skm = tbl['e_z_skm'][i],
            starhorse_dist05 = tbl['starhorse_dist05'][i],
            starhorse_dist16 = tbl['starhorse_dist16'][i],
            starhorse_dist50 = tbl['starhorse_dist50'][i],
            starhorse_dist84 = tbl['starhorse_dist84'][i],
            starhorse_dist95 = tbl['starhorse_dist95'][i],
            decam_g = tbl['decam_g'][i],
            decam_r = tbl['decam_r'][i],
            decam_i = tbl['decam_i'][i],
            decam_z = tbl['decam_z'][i],
            decam_phot_src_bits = tbl['decam_phot_src_bits'][i],
            qso_flag_wise = tbl['qso_flag_wise'][i],
            priority = tbl['priority'][i],
            primary = tbl['primary'][i],
            moon_phase = tbl['moon_phase'][i],
            moon_alt = tbl['moon_alt'][i],
            moon_dist = tbl['moon_dist'][i],
            good_star_pb = tbl['good_star_pb'][i],
            good_star = tbl['good_star'][i],
            vel_calib = tbl['vel_calib'][i],
            vel_calib_std = tbl['vel_calib_std'][i],
            feh_calib_std = tbl['feh_calib_std'][i])
            s.save()
        return
    
    
    