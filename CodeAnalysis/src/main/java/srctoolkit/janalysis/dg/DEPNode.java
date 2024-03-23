/*** In The Name of Allah ***/
package srctoolkit.janalysis.dg;


import org.antlr.v4.runtime.ParserRuleContext;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

/**
 * Class type of Control Flow (CF) nodes.
 * 
 * @author Seyed Mohammad Ghaffarian
 */
public class DEPNode {
	private Map<String, Object> properties;
	private Set<String> DEFs, USEs, selfFlows;

	
	public DEPNode() {
		DEFs = new HashSet<>();
		USEs = new HashSet<>();
		selfFlows = new HashSet<>();
		properties = new LinkedHashMap<>();
	}
	
	public void setLineOfCode(int line) {
		properties.put("line", line);
	}
	
	public int getLineOfCode() {
		return (Integer) properties.get("line");
	}
	
	public void setCode(String code) {
		properties.put("code", code);
	}
	
	public String getCode() {
		return (String) properties.get("code");
	}

	public void setAbstract(String abs) {
		properties.put("abstract", abs);
	}

	public String getAbstract() {
		return (String) properties.get("abstract");
	}

	public void setRuleCtx(ParserRuleContext ctx) {
		properties.put("rulectx", ctx);
	}
    
    public ParserRuleContext getRuleCtx() {
        return (ParserRuleContext) getProperty("rulectx");
    }

	public boolean addDEF(String var) {
		return DEFs.add(var);
	}

	public boolean hasDEF(String var) {
		return DEFs.contains(var);
	}

	public String[] getAllDEFs() {
		return DEFs.toArray(new String[DEFs.size()]);
	}

	public boolean addUSE(String var) {
		return USEs.add(var);
	}

	public boolean hasUSE(String var) {
		return USEs.contains(var);
	}

	public String[] getAllUSEs() {
		return USEs.toArray(new String[USEs.size()]);
	}

	public boolean addSelfFlow(String var) {
		return selfFlows.add(var);
	}

	public String[] getAllSelfFlows() {
		return selfFlows.toArray(new String[selfFlows.size()]);
	}
	
	public void setProperty(String key, Object value) {
		properties.put(key.toLowerCase(), value);
	}
	
	public Object getProperty(String key) {
		return properties.get(key.toLowerCase());
	}
	
	public Set<String> getAllProperties() {
		return properties.keySet();
	}
	
	@Override
	public String toString() {
		return (Integer) properties.get("line") + ": " + 
				(String) properties.get("code");
	}
}
