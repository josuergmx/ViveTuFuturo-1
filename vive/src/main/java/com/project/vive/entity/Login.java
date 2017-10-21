package com.project.vive.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "login")
public class Login {
	@Id
	@GeneratedValue
	@Column(name = "idusuario")
	private String id;
	
	@Column(name = "password")
	private String password;
	
	@Column(name = "idrole")
	private Integer idRole;
	
	@Column(name = "idpersona")
	private Integer idPersona;
	
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "idrole", updatable = false, insertable = false)
	private Rol rol;
	
	@OneToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "idpersona", updatable = false, insertable = false)
	private Persona persona;

	public Login(){
		super();
	}
	
	public Login(String id, String password, Integer idRole, Integer idPersona, Rol rol, Persona persona) {
		super();
		this.id = id;
		this.password = password;
		this.idRole = idRole;
		this.idPersona = idPersona;
		this.rol = rol;
		this.persona = persona;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Integer getIdRole() {
		return idRole;
	}

	public void setIdRole(Integer idRole) {
		this.idRole = idRole;
	}

	public Integer getIdPersona() {
		return idPersona;
	}

	public void setIdPersona(Integer idPersona) {
		this.idPersona = idPersona;
	}

	public Rol getRol() {
		return rol;
	}

	public void setRol(Rol rol) {
		this.rol = rol;
	}

	public Persona getPersona() {
		return persona;
	}

	public void setPersona(Persona persona) {
		this.persona = persona;
	}
	
	
}
