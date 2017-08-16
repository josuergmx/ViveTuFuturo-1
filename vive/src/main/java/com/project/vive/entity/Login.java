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
	
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "idrole")
	private Rol idRole;
	
	@OneToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "idpersona")
	private Persona idPersona;

	public Login(){
		super();
	}
	
	public Login(String id, String password, Rol idRole, Persona idPersona) {
		super();
		this.id = id;
		this.password = password;
		this.idRole = idRole;
		this.idPersona = idPersona;
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

	public Rol getIdRole() {
		return idRole;
	}

	public void setIdRole(Rol idRole) {
		this.idRole = idRole;
	}

	public Persona getIdPersona() {
		return idPersona;
	}

	public void setIdPersona(Persona idPersona) {
		this.idPersona = idPersona;
	}
	
	
}
