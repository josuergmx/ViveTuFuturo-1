package com.project.vive.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name="direccion")
public class Direccion {
	@Id
	@GeneratedValue
	@Column(name = "iddireccion")
	private Integer id;
	
	@ManyToOne(fetch=FetchType.EAGER)
	@JoinColumn(name = "idpersona")
	private Persona propietario;
	
	@ManyToOne(fetch=FetchType.EAGER)
	@JoinColumn(name = "idtipodireccion")
	private TipoDireccion tipoDireccion;
	
	@Column(name = "calle")
	private String calle;
	
	@Column(name = "colonia")
	private String colonia;
	
	@Column(name = "delegacion")
	private String delegacion;
	
	@Column(name = "cp")
	private String cp;
	
	@Column(name = "numinterior")
	private String numeroInterior;
	
	@Column(name = "numexterior")
	private String numeroExterior;
	
	public Direccion(){
		super();
	}

	public Direccion(Integer id, Persona propietario, TipoDireccion tipoDireccion, String calle, String colonia,
			String delegacion, String cp, String numeroInterior, String numeroExterior) {
		super();
		this.id = id;
		this.propietario = propietario;
		this.tipoDireccion = tipoDireccion;
		this.calle = calle;
		this.colonia = colonia;
		this.delegacion = delegacion;
		this.cp = cp;
		this.numeroInterior = numeroInterior;
		this.numeroExterior = numeroExterior;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Persona getPropietario() {
		return propietario;
	}

	public void setPropietario(Persona propietario) {
		this.propietario = propietario;
	}

	public TipoDireccion getTipoDireccion() {
		return tipoDireccion;
	}

	public void setTipoDireccion(TipoDireccion tipoDireccion) {
		this.tipoDireccion = tipoDireccion;
	}

	public String getCalle() {
		return calle;
	}

	public void setCalle(String calle) {
		this.calle = calle;
	}

	public String getColonia() {
		return colonia;
	}

	public void setColonia(String colonia) {
		this.colonia = colonia;
	}

	public String getDelegacion() {
		return delegacion;
	}

	public void setDelegacion(String delegacion) {
		this.delegacion = delegacion;
	}

	public String getCp() {
		return cp;
	}

	public void setCp(String cp) {
		this.cp = cp;
	}

	public String getNumeroInterior() {
		return numeroInterior;
	}

	public void setNumeroInterior(String numeroInterior) {
		this.numeroInterior = numeroInterior;
	}

	public String getNumeroExterior() {
		return numeroExterior;
	}

	public void setNumeroExterior(String numeroExterior) {
		this.numeroExterior = numeroExterior;
	}
	
}
