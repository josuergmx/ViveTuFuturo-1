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
@Table(name = "contacto")
public class Contacto {
	@Id
	@GeneratedValue
	@Column(name = "celular")
	private Integer celular;
	
	@Column(name = "email")
	private String  email;
	
	@Column(name = "telcasa")
	private String telcasa;
	
	@Column(name = "oficina")
	private String oficina;
	
	@Column(name = "facebookid")
	private String facebookId;
	
	@ManyToOne(fetch=FetchType.EAGER)
	@JoinColumn(name = "idpersona")
	private Persona propietario;

	public Contacto(){
		super();
	}
	
	
	
	public Contacto(Integer celular, String email, String telcasa, String oficina, String facebookId,
			Persona propietario) {
		super();
		this.celular = celular;
		this.email = email;
		this.telcasa = telcasa;
		this.oficina = oficina;
		this.facebookId = facebookId;
		this.propietario = propietario;
	}



	public Integer getCelular() {
		return celular;
	}

	public void setCelular(Integer celular) {
		this.celular = celular;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getTelcasa() {
		return telcasa;
	}

	public void setTelcasa(String telcasa) {
		this.telcasa = telcasa;
	}

	public String getOficina() {
		return oficina;
	}

	public void setOficina(String oficina) {
		this.oficina = oficina;
	}

	public String getFacebookId() {
		return facebookId;
	}

	public void setFacebookId(String facebookId) {
		this.facebookId = facebookId;
	}

	public Persona getPropietario() {
		return propietario;
	}

	public void setPropietario(Persona propietario) {
		this.propietario = propietario;
	}
	
	
}
